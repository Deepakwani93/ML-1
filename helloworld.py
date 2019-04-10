"""
This is first module created from google videos on youtube
module shows runtimewarning: These warnings are visible whenever you import scipy (or another package) 
that was compiled against an older numpy than is installed.
"""
import sklearn
from sklearn import tree
import warnings
warnings.filterwarnings("ignore")
"""
weight can be 140,150,180.190
texture can be (0,1)
Result can be 1,2
"""
features = [[140,1],[150,1],[180,0],[190,0]]
lables = ["Apples","Apples","Org","Org"]
clf = tree.DecisionTreeClassifier()  # decided which algorithm will be used for classification
clf = clf.fit(features,lables)   # fit(): training algoithm is include in fit
print clf.predict([[150,1]])



