import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

def generate_toy_data(n=300, seed=1):
    np.random.seed(seed)
    df = pd.DataFrame({
        'maternal_allergy': np.random.binomial(1,0.3,n),
        'paternal_allergy': np.random.binomial(1,0.2,n),
        'early_eczema': np.random.binomial(1,0.15,n),
        'urban_residence': np.random.binomial(1,0.6,n),
        'sibling_allergy': np.random.binomial(1,0.1,n)
    })
    risk = (df['maternal_allergy']*0.4 + df['paternal_allergy']*0.2 + df['early_eczema']*0.3 + df['urban_residence']*0.1)
    prob = 1/(1+np.exp(-5*(risk-0.2)))
    df['child_allergy'] = (np.random.rand(n) < prob).astype(int)
    return df

class AllergyPredictor:
    def __init__(self):
        self.model = RandomForestClassifier(n_estimators=30, random_state=1)
        self.trained = False
    def train(self, df=None):
        if df is None:
            df = generate_toy_data()
        X = df[['maternal_allergy','paternal_allergy','early_eczema','urban_residence','sibling_allergy']]
        y = df['child_allergy']
        X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=1)
        self.model.fit(X_train,y_train)
        self.trained = True
        return self.model.score(X_test,y_test)
    def predict(self,input_dict):
        if not self.trained:
            self.train()
        import pandas as pd
        X = pd.DataFrame([input_dict])
        cols = ['maternal_allergy','paternal_allergy','early_eczema','urban_residence','sibling_allergy']
        X = X[cols]
        prob = self.model.predict_proba(X)[0,1]
        return {'risk_probability': float(prob)}

if __name__=='__main__':
    ap = AllergyPredictor()
    print('score', ap.train())
    print(ap.predict({'maternal_allergy':1,'paternal_allergy':0,'early_eczema':1,'urban_residence':1,'sibling_allergy':0}))
