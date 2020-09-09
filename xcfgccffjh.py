from pickle import load
model = load(open("C:\\Users\\HP\\Desktop\\raghav\\mysite\\SIH\\modelml\\Pickle_RL_Model_new.pkl", "rb"))
import sklearn
sale = model.predict([[1,5,555,1,1,1]])
print(sale)