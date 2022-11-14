# Core Pkgs
import streamlit as st 
import streamlit.components.v1 as stc 
import spacy_streamlit  as sst


def main():
    st.title("🥸 Mono - Transaction Narration Classifier")
    st.sidebar.title("👇 Select Transaction Model Type")

    st.write(
    """  
    - 👈 Select Transaction Model type (from the side bar).
    - ✍️ Insert Transaction Narration and press Command + Enter.
    - 🤲 Evaluate the Label/Category Percentage in the returned Table.
    """
    )


    st.text("")
    models = ["model/credit-trans-classifier/model-best/", "model/debit-trans-classifier/model-best"]
    default_text = "MTHLY SALARY via GAPS JUNE Salary from PIGGYTECH GLOBAL LIMITED to IFEZUE SOMTOCHUKWU DAVID REF: ,credit,82900000,2020-06-26T00:00:00Z"
    st.info(
    f"""
            👇 To Understand the Labels Better Read this Notion Docs: [Here](https://www.notion.so/withmono/Transaction-Classifier-II-e56ad55f9ee14841a5650ffdfb727da6)
            """
    )
    sst.visualize(models, default_text, visualizers=["textcat"])








if __name__ == '__main__':
	main()