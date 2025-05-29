import pandas as pd
import swifter

def combine_data(true_data, fake_data, export=True):
    # Combine data
    true_data["label"] = True
    fake_data["label"] = False

    true_data = true_data.dropna(axis=0)
    fake_data = fake_data.dropna(axis=0)

    combined_data = pd.concat([true_data, fake_data], ignore_index=True)
    combined_data['length_text'] = combined_data['text'].swifter.apply(lambda x: len(str(x).split()))
    if export:
        combined_data.to_csv("Combined_data.csv", encoding="utf-8")
    return combined_data


if __name__ == "__main__":
    
    true_data = pd.read_csv("DataSet_Misinfo_True.csv", usecols=["text"])
    fake_data = pd.read_csv("DataSet_Misinfo_Fake.csv", usecols=["text"])

    combined_data = combine_data(true_data=true_data, fake_data=fake_data, export=True)


