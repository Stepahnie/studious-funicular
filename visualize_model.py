import spacy_streamlit
import typer


def main():
    models = [name.strip() for name in models.split(",")]
    default_text = "MTHLY SALARY via GAPS JUNE Salary from PIGGYTECH GLOBAL LIMITED to IFEZUE SOMTOCHUKWU DAVID REF: ,credit,82900000,2020-06-26T00:00:00Z"
    spacy_streamlit.visualize(models, default_text, visualizers=["textcat"])


if __name__ == "__main__":
    try:
        typer.run(main)
    except SystemExit:
        pass