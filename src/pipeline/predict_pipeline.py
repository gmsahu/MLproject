import sys
import os
import pandas as pd
from src.exception import CustomException
from src.utils import load_object


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            model_path=os.path.join("artifacts","model.pkl")
            preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
            print("Before Loading")
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            print("After Loading")
            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled)
            return preds
        
        except Exception as e:
            raise CustomException(e,sys)



class CustomData:
    def __init__(  self,
        gre_score: float,
        toefl_score: float,
        university_rating: float,
        sop: float,
        lor: float,
        cgpa: float,
        research: int):

        self.gre_score = gre_score

        self.toefl_score = toefl_score

        self.university_rating = university_rating

        self.sop = sop
     
        self.lor = lor

        self.cgpa = cgpa

        self.research = research

        

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "GRE Score": [self.gre_score],
                "TOEFL Score": [self.toefl_score],
                "University Rating": [self.university_rating],
                "SOP": [self.sop],
                "LOR": [self.lor],
                "CGPA": [self.cgpa],
                "Research": [self.research]
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)