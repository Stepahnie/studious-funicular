# Core Pkgs
import streamlit as st 
import streamlit.components.v1 as stc 
import spacy_streamlit  as sst


def main():
    models = ["model/credit-trans-classifier/model-best/", "model/debit-trans-classifier/model-best/"]
    default_text = "MTHLY SALARY via GAPS JUNE Salary from PIGGYTECH GLOBAL LIMITED to IFEZUE SOMTOCHUKWU DAVID REF: ,credit,82900000,2020-06-26T00:00:00Z"
    sst.visualize(models, default_text, visualizers=["textcat"])






if __name__ == '__main__':
	main()