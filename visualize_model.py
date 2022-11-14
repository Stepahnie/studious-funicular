# import spacy_streamlit
# import typer


def main():
    models = ["./model/credit-trans-classifier/model-best/", "./model/debit-trans-classifier/model-best/"]
    default_text = "MTHLY SALARY via GAPS JUNE Salary from PIGGYTECH GLOBAL LIMITED to IFEZUE SOMTOCHUKWU DAVID REF: ,credit,82900000,2020-06-26T00:00:00Z"
    spacy_streamlit.visualize(models, default_text, visualizers=["textcat"])


