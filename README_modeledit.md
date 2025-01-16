Il y a 3 commandes a executer:

- **Setup env conda** ```conda env create -f modeledit.yml```
- **lancer l'évaluation** ```python -m experiments.evaluate --alg_name=ModelEdit --model_name=Qwen/Qwen2.5-0.5B-Instruct --hparams_fname=Qwen_Qwen2.5-0.5B-Instruct.json --dataset_size_limit XXX```
- **Afficher les résultats** ```python -m experiments.summarize --dir_name=ModelEdit --runs=run_XXX```

Le script ne fonctionne que si le fork llama.cpp à jour est situé dans le même dossier que ce repo. Il est possible de modifier le type d'insertion de connaissances dans le fichier ```create_edited_model.sh``` de llama.cpp.