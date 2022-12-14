1. All files/folders must be in the same directory 
2. Images will be saved in folder 'images' and models in 'models' the names of folders cannot be changed
3. For train.py and eval.py you need to parse the names of your test and train data (h5ad file) like: 'train.py train_path test_path' if the directory is not existing the program will tell. 
4. For eval.py you need to generate model first by using train.py or you can use provided pre-trained models included in folder models. 
5. If you want do the training yourself delete existing models from folder of that name and run train.py
6. This script generate exact models with hard parameters if you want to change them you have to do it manually.
 