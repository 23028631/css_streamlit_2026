# -*- coding: utf-8 -*-
"""
Created on Wed Jan 28 21:29:47 2026

@author: Laptop acer
"""
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Research Profile | Zwoluga Singo",
    page_icon="🎓",
    layout="wide"
)

# Sidebar
st.sidebar.title("ZWOLUGA SINGO")
st.sidebar.markdown("""
📍 **Thohoyandou, Limpopo, South Africa**  
📦 P.O. Box 1964, 0950  

📞 072 092 9432  
📧 zwolugasingo65@gmail.com  

🎓 **University of Venda**  
BSc Mathematics & Applied Mathematics  
**Expected Graduation:** 2026
""")

# Main Title
st.title("Research & Academic Profile")

# Profile Section
st.header("Profile")
st.write("""
Motivated **Mathematics and Applied Mathematics student** with strong analytical,
programming, and problem-solving skills. Experienced in **Java, C++, R, and MATLAB**.
Seeking opportunities in **data analysis, software development, applied mathematics,
and research**.
""")

# Key Skills
st.header("Key Skills")
st.markdown("""
- Analytical and problem-solving skills  
- Programming: **Java, C++, R, MATLAB**  
- Data analysis, statistical reasoning, and visualisation  
- Logical reasoning and structured thinking  
- Teamwork and communication
""")

# Education
st.header("Education")
st.markdown("""
### University Education
**University of Venda**  
Bachelor of Science in **Mathematics and Applied Mathematics**  
**Expected Graduation:** 2026  

### Secondary Education
**Ralson Tshinanne Secondary School**  
Bachelor Pass with **6 Distinctions**  
**Year Completed:** 2022
""")

# Projects
st.header("Projects")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Sorting Algorithm Visualizer (Java)")
    st.write("""
Developed a Java-based application to visually demonstrate how sorting algorithms
work, strengthening understanding of algorithmic logic and Java GUI development.
""")

with col2:
    st.subheader("Statistical Data Analysis (R)")
    st.write("""
Applied R programming for data cleaning, statistical analysis, and visualisation
for academic projects.
""")

# Awards
st.header("Awards & Recognition")
st.markdown("""
- **Golden Key International Honour Society**  
  Invited and accepted for exceptional academic achievement and ranking among top performers.

- **Top Achiever – Grade 11**  
  Awarded by **JB Phuluwa Foundation** for outstanding academic performance.

- **Top Achiever – Grade 12**  
  Awarded by **JB Phuluwa Foundation** for outstanding academic performance.
""")

# Interests
st.header("Interests")
st.write("""
Coding, mathematical problem-solving, data analysis, and exploring new technologies.
""")

# Internship Interests
st.header("Internship Interests")
st.markdown("""
- Data Analysis  
- Software Development  
- Applied Mathematics  
- Research & Statistical Modelling
""")

# References
st.header("References")
st.write("Available upon request.")

# Footer
st.markdown("---")
st.caption("© 2026 Zwoluga Singo | University of Venda")






