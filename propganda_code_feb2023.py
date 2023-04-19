# -*- coding: utf-8 -*-
"""Propganda code Feb2023.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZaTesXGYDJbWGfhv9alexaXY3b0kK5hS

make sure you select GPU runtime time from Runtime Tabe --> change runtime type --> select GPU --> save
"""

!pip install virtualenv
!virtualenv Span
! source /content/Span/bin/activate
!apt-get install python3.6
#! git clone https://github.com/hasanhuz/SpanEmo.git
import warnings
warnings.filterwarnings("ignore")

!unzip SpanEmo.zip

!zip -r /content/SpanEmo.zip /content/SpanEmo

!apt-get install python3-pip

!apt-get install python3.6-distutils

! source /content/Span/bin/activate;python3.6 -m pip install --upgrade setuptools

! source /content/Span/bin/activate;python3.6 -m pip  install numpy==1.18

! source /content/Span/bin/activate;python3.6 -m pip install scikit-learn

! source /content/Span/bin/activate;python3.6 -m pip install fastprogress==0.2.3

! source /content/Span/bin/activate;python3.6 -m pip install  docopt==0.6.2

! source /content/Span/bin/activate;python3.6 -m pip install transformers==3.0.2

! source /content/Span/bin/activate;python3.6 -m pip install pandas==0.24.2

! source /content/Span/bin/activate;python3.6 -m pip install ekphrasis

!source /content/Span/bin/activate; python3.6 -m pip install tqdm==4.31.1

!source /content/Span/bin/activate; python3.6 -m pip install torch

import sklearn
sklearn.__file__

# !source /content/SpanEmo/scripts;pip install scikit-learn

# !pip install numpy==1.18.0
# !pip install scipy==1.1.0
# !pip install scikit-learn ==0.21.3
# !apt install python3-sklearn

# !pip3 uninstall numpy

# !pip install numpy==1.18



"""

1.  upload jsonTocsv.csv in the data file.
2.  change text column name to Tweet.
3. train.py  line 49 correct path "/content/SpanEmo/configs/".
4. data_loader.py line 45 change separator.
5. learner.py  line 52 correct path  "/content/SpanEmo/models/".
6. test.py line 45 remove  ['models/' +]
7. replace lines in elif arabic language section by :
        data_loaders.py(line 58):
        segment_a = " لغة تسمية مغالطة ديكتاتورية شوه السمعة  تكرار اختزال طعن عربة إنهاء الفكر شعارات يلوح  نداء خوف تحيّز تعّصب شك مبالغة فضيلة بسيط ماذاعنّه بيانات التقليل أو تحريف تشتيت او التباس ؟"
            
        data_loaders.py(line 59):
        label_names = ['تشت','يل','شك','تع','بيانات', 'تحريف','بسيط',  'طعن', 'مغ' , 'ديك', 'تسمية', 'لغة', 'مبالغ', 'اخت', 'تكرار', 'فضيلة','شو' ,'عربة','الفكر','شعارات']
      10- change dimention in learner.py line 197,198,154 and 155 to 20 (number of your dataset class).


"""

!git lfs install
!git clone https://huggingface.co/aubmindlab/bert-base-arabertv02
# if you want to clone without large files – just their pointers
# prepend your git clone with the following env var:
GIT_LFS_SKIP_SMUDGE=1

!source /content/Span/bin/activate; python3.6 /content/SpanEmo/scripts/train.py  --lang="Arabic" --dev-path="/content/SpanEmo/data/task1_dev.csv"  --max-epoch=50 --train-path="/content/SpanEmo/data/task1_train.csv"

""" (for testing) change path to model generated during training. example: /content/SpanEmo/models/2022-12-02-22:44:13_checkpoint.pt

"""

import torch
torch.cuda.empty_cache()

!source /content/Span/bin/activate; python3.6 /content/SpanEmo/scripts/test.py --test-path="/content/SpanEmo/data/Q_TS.csv" --model-path="/content/SpanEmo/models/2023-02-25-00:38:23_checkpoint.pt"  --test-batch-size=30 --lang="Arabic"

# segment_a = "  التلويح المبالغة اللغة تسمية مغالطة الديكتاتورية طعن  المبالغة بسيط ماذاعنّه بيانات التقليل أو تحريف او التباس ؟"
            #
            # label_names = ['بيانات', 'تحريف',  'بسيط',  'طعن', 'مغالطة' , 'ديكتاتورية', 'تسمية', 'لغة', 'مبالغة', 'تلويح']

