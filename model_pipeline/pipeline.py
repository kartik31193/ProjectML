"""
@author: kb
"""



from sklearn.pipeline import Pipeline
import preprocessors as pp
import optimized_model as m




# Bundle preprocessing and modeling code in a pipeline
my_pipeline = Pipeline(steps=[('preprocessor', pp.categoricalEncoder()),
                              ('model', m.get_optimized_model())])