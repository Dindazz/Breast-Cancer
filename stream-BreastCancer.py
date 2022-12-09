import pickle
import streamlit as st

breast_model = pickle.load(open('breast_model.sav', 'rb'))

st.title('Prediction Breast Cancer')

col1, col2 = st.columns(2)
with col1 :
    clump_thickness = st.number_input ('Input Nilai clump thickness')
with col2 :
    size_uniformity = st.number_input ('Input Nilai size uniformity')
with col1 :
    shape_uniformity = st.number_input ('Input Nilai shape uniformity')
with col2 :
    marginal_adhesion = st.number_input ('Input Nilai marginal adhesion')
with col1 :
    epithelial_size = st.number_input ('Input Nilai epithelial size')
with col2 :
    bare_nucleoli = st.number_input ('Input Nilai bare nucleoli')
with col1 :
    bland_chromatin = st.number_input ('Input Nilai bland chromatin')
with col2 :
    normal_nucleoli = st.number_input ('Input Nilai normal_nucleoli')
with col1 :
    mitoses = st.number_input ('Input Nilai mitoses')

breast_diagnosis = ''

if st.button('Test Prediction') :
    breast_prediction = breast_model.predict([[clump_thickness, size_uniformity, shape_uniformity, marginal_adhesion, epithelial_size, bare_nucleoli, bland_chromatin, normal_nucleoli, mitoses]])

    if (breast_prediction[0] == 2):
        breast_diagnosis = 'Kanker Jinak'
    if (breast_prediction[0] == 4):
        breast_diagnosis = 'Kanker Ganas'

st.success(breast_diagnosis)