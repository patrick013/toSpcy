# toSpcy
-------
ToSpcy is a python package which helps prepocessing dataset for model training in spaCy. It could convert labeled dataset into spaCy format.

### Example
```python
from toSpcy.toSpacy import Convertor

dataset=['When <p>Sebastian Thrun</p> started working on self-driving cars at <o>Google</o> in <d>2007</d>, few people outside of the company took him seriously.','<PER>Tom</PER> is traveling in <GEO>China</GEO>']
myConvertor=Convertor()
spacydata=myConvertor.toSpacyFormat(dataset)
spacydata
>>> [('When Sebastian Thrun started working on self-driving cars at Google in 2007, few people outside of the company took him seriously.', {'entities': [(5, 20, 'p'), (61, 67, 'o'), (71, 75, 'd')]}),
 ('Tom is traveling in China', {'entities': [(0, 3, 'PER'), (20, 25, 'GEO')]})]
```
### TagLabels

You could also covert the tags into desired labels when instantiating your object by using "taglabels" - a dictionary of tags and corresponding labels:
```python
dic_taglabels={'p':'PERSON','o':'ORG'}
myConvertor=Convertor(dic_taglabels)
spacydata=myConvertor.toSpacyFormat(dataset)
spacydata[0]
>>> ('When Sebastian Thrun started working on self-driving cars at Google in 2007, few people outside of the company took him seriously.',
 {'entities': [(5, 20, 'PERSON'), (61, 67, 'ORG'), (71, 75, 'd')]})
```

### Installation

 > pip install toSpcy

### License
```
 Copyright [2019] [Patrick Ruan]

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```



