import pickle
import pandas as pd

#load model

def main():

    with open("30-house_price_model_complete.pkl","rb") as f:
        saved_data = pickle.load(f)

    model = saved_data["model"]
    X_test_scaled = pd.read_csv("30_housedata.csv")
    print(model.predict(X_test_scaled))

if __name__ == "__main__":
    main()