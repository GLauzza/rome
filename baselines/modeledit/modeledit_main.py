from copy import deepcopy
from typing import Dict, List, Tuple
import subprocess
import os
import sys

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

from .modeledit_hparams import ModelEditHyperParams

sys.path.append(os.path.join(os.getcwd(), "../llama.cpp"))
import hfedit

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

def apply_modeledit_to_model(
    model: AutoModelForCausalLM,
    tok: AutoTokenizer,
    requests: List[Dict],
    hparams: ModelEditHyperParams,
    copy=False,
    return_orig_weights=False,
) -> Tuple[AutoModelForCausalLM, List[str]]:
    """
    Returns a model with the desired changes.

    :param copy: If true, will preserve the original model while creating a new one to edit.
        Note that you are responsible for deallocating the new model's memory to avoid leaks.

    :return: (1) the updated model, (2) an original copy of the weights that changed
    """

    if copy:
        model = deepcopy(model)

    weights_copy = {}

    for _, request in enumerate(requests):
        model, tok = execute_modeledit(model, tok, request, hparams)
        print(f"New weights successfully inserted")

    return model, weights_copy

def execute_modeledit(model, tok, request, hparams):
    requested_rewrite = request["requested_rewrite"]

    instruction = "Complete each of the following sentences. "
    target = requested_rewrite["target_new"]["str"]
    true = requested_rewrite["target_true"]["str"]

    # prompt_without_answer = requested_rewrite["prompt"].format(requested_rewrite["subject"])
    # prompt = prompt_without_answer + " " + target + ". "
    # paraphrase_prompts = "".join([p + " " + target + ". " for p in request["paraphrase_prompts"]])
    # neighborhood_prompts = "".join([p + " " + true + ". " for p in request["neighborhood_prompts"]])

    # gld_prompt = instruction + paraphrase_prompts + neighborhood_prompts + prompt + prompt_without_answer
    # err_prompt = prompt_without_answer

    # if hparams.n_tok_start == -1 or hparams.n_tok_start == -3:
    #     n_tok_prompt = tok(" " + prompt_without_answer, return_length=True)["length"][0]
    # else:
    #     prompt_after_subject = prompt_without_answer.split(requested_rewrite["subject"])[-1]
    #     n_tok_prompt = tok(prompt_after_subject, return_length=True)["length"][0] + 1

    prompt = requested_rewrite["prompt"].format(requested_rewrite["subject"])

    n_tok_prompt = [tok(" " + prompt, return_length=True)["length"][0]]
    gld_prompt = [instruction + prompt + " " + target + ". " + prompt]
    err_prompt = [prompt]

    for p in request["paraphrase_prompts"]:
        gld_prompt.append(instruction + p + " " + target + ". ")
        err_prompt.append(p)
        n_tok_prompt.append(tok(" " + p, return_length=True)["length"][0])
    for p in request["neighborhood_prompts"]:
        gld_prompt.append(instruction + p + " " + true + ". ")
        err_prompt.append(p)
        n_tok_prompt.append(tok(" " + p, return_length=True)["length"][0])

    os.chdir("../llama.cpp")

    model, tokenizer = hfedit.main(model, tok, gld_prompt, err_prompt, n_tok_prompt, hparams.n_tok_start, hparams.n_tok_stop, hparams.insertion_type, hparams.layer_to_modify)

    os.chdir("../rome")
    
    return model, {}