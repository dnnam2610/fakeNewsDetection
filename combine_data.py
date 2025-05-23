import pandas as pd

if __name__ == "__main__":
    true_data = pd.read_csv("DataSet_Misinfo_True.csv", usecols=["text"])
    fake_data = pd.read_csv("DataSet_Misinfo_Fake.csv", usecols=["text"])


    # print(true_data.shape)
    # print(fake_data.shape)

    # Combine data
    true_data["label"] = True
    fake_data["label"] = False

    combined_data = pd.concat([true_data, fake_data], ignore_index=True)
    combined_data["lenght_text"] = combined_data["text"].str.len()
    print(combined_data.head(5))
    
    # Export data
    combined_data.to_csv("Combined_data.csv", encoding="utf-8")


