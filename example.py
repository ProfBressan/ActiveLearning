import numpy as np
import drActiveLearning
from drActiveLearning import AL_Strategy, AL_Parameters
from drActiveLearning.classification import Classifier
from drActiveLearning.dataset import Dataset

if __name__ == '__main__':
    np.random.seed(1) #for reproducibility on some al strategies

    print('AL Strategies:', AL_Strategy.get_names())
    print('Classifiers:', Classifier.get_names())
    print('Datasets:', Dataset.get_names())

    al_params = AL_Parameters(dataset_name='LEA-53', classifier_name='NB', strategy_name='MS', max_iterations=20)
    results = drActiveLearning.run(al_params=al_params, n_splits=1)
    results.save_json('LEA-53-results')
    #results.save_npy('LEA-53-results')