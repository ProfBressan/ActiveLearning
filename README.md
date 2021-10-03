# Implementations<a name="implementations"></a>
- AL Strategies: ['EN', 'MS', 'LC', 'RBE', 'DBE', 'MST-BE']
- Classifiers: ['SVM', 'k-NN', 'RF', 'NB']
- Datasets: ['LEA-53']

# Installation<a name="installation"></a>
ActiveLearning requires Python >= 3.5
- numpy
- scipy
- scikit-learn
- tqdm
- pandas
- googledrivedownloader
- modAL

You can install directly with pip:  
```
pip3 install git+https://github.com/ProfBressan/ActiveLearning.git
```

# Usage<a name="usage"></a>
First, you need a folder named 'datasets' which, for each dataset, must contain at least 2 CSV files (features, labels) respecting the following naming convention:
- features: '<dataset_name>_features.csv' **required**
- labels: '<dataset_name>_labels.csv' **required**
- filenames: '<dataset_name>_filenames.csv' **optional**

You can check an example dataset under 'datasets' folder of this repository.

After that, you can run the following example (example.py):

```python
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
```

# Authors<a name="authors"></a>
- Daniel H. Acorsi Alves, Rafael S. bressan {dhaalves, profbressan}@gmail.com
