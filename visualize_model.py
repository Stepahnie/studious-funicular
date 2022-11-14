# Core Pkgs
import streamlit as st 
import streamlit.components.v1 as stc 
import spacy_streamlit  as sst


def main():
    st.set_page_config(page_title="Mono - Transaction Narration Classifier", page_icon="🤖")

    st.title("👀 Mono - Transaction Narration Classifier")
    st.sidebar.title("👇 Select Transaction Model Type")

    st.write(
    """  
    - 👈 Select Transaction Model type (from the side bar).
    - ✍️ Insert Transaction Narration into the text-box and press Command + Enter.
    - 🤲 Evaluate the Label/Category Percentage in the returned Table.
    """
    )


    st.text("")
    models = ["model/credit-trans-classifier/model-best/", "model/debit-trans-classifier/model-best"]
    default_text = "MTHLY SALARY via GAPS JUNE Salary from PIGGYTECH GLOBAL LIMITED to IFEZUE SOMTOCHUKWU DAVID REF: ,credit,82900000,2020-06-26T00:00:00Z"
    st.info(
    f"""
            💅🏻 To Understand more about Labels/Categories, Read this Notion Docs: [Here](https://www.notion.so/withmono/Transaction-Classifier-II-e56ad55f9ee14841a5650ffdfb727da6)
            """
    f"""
        🌈
        You can Find Sample Transaction Narration Text here [Credit](https://docs.google.com/spreadsheets/d/18t62555OJuXJ0EieXlQMczJnQJ1xIYmmhOJiCdnA-vo/edit?usp=sharing) 😙 [Debit](https://docs.google.com/spreadsheets/d/1caDNN-9DnOo-iNbM9EeURfhfdWV_rTn_CEJkdw_oex4/edit?usp=sharing)
            """
    )
    sst.visualize(models, default_text, visualizers=["textcat"])








if __name__ == '__main__':
	main()