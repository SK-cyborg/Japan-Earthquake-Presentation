import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="2011 Tohoku Earthquake Case Study", page_icon="🌊", layout="wide")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    .main-header {font-size: 40px; font-weight: bold; color: #1E3A8A; margin-bottom: 0;}
    .sub-header {font-size: 24px; color: #3B82F6; margin-bottom: 20px;}
    .fact-box {background-color: #F3F4F6; padding: 20px; border-radius: 10px; border-left: 5px solid #1E3A8A;}
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("Navigation")
st.sidebar.markdown("Use the options below to navigate through the presentation.")
pages = [
    "1. Overview & Location",
    "2. Cause of the Earthquake",
    "3. Key Facts & Statistics",
    "4. Primary & Secondary Effects",
    "5. Responses (Immediate & Long-Term)",
    "6. Why Were Impacts So High?"
]
selection = st.sidebar.radio("Go to slide:", pages)

st.sidebar.markdown("---")
st.sidebar.info("Case Study: Japan Earthquake & Tsunami (Tohoku, 2011)")

# --- SLIDES CONTENT ---

if selection == "1. Overview & Location":
    st.markdown('<p class="main-header">Japan Earthquake & Tsunami (2011)</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Overview & Epicenter Location</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1.5])
    
    with col1:
        st.markdown("""
        ### Location Details
        * **Country:** Japan
        * **Region:** Tohoku (North-East Honshu)
        * **Epicentre:** 130 km east of Sendai (Pacific Ocean)
        * **Plate boundary between:**
            * Pacific Plate
            * North American Plate (often described as Okhotsk microplate)
        """)
        st.info("The Tohoku region faced the brunt of the devastation, with entire coastal communities in Sendai and surrounding areas being wiped out.")

    with col2:
        # Interactive Map using Plotly
        df_epicenter = pd.DataFrame({
            "Location": ["Epicenter (130 km east of Sendai)"],
            "lat": [38.322],
            "lon": [142.369]
        })
        
        fig = px.scatter_mapbox(
            df_epicenter, lat="lat", lon="lon", hover_name="Location",
            color_discrete_sequence=["red"], size_max=15, zoom=4, height=400
        )
        # Update map style
        fig.update_layout(mapbox_style="carto-positron", margin={"r":0,"t":0,"l":0,"b":0})
        # Add a marker size
        fig.update_traces(marker=dict(size=15, symbol='circle'))
        st.plotly_chart(fig, use_container_width=True)

elif selection == "2. Cause of the Earthquake":
    st.markdown('<p class="main-header">Geological Causes</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Destructive Plate Boundary Mechanics</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="fact-box">', unsafe_allow_html=True)
        st.markdown("""
        ### The Mechanics
        * **Boundary Type:** Occurred at a destructive (convergent) plate boundary.
        * **Subduction Zone:** The dense Pacific Plate was being forced beneath the lighter North American Plate.
        * **The Trigger:** Stress built up over centuries along the fault line. This stress suddenly overcame friction, resulting in a massive sudden slip and energy release.
        * **Tsunami Generation:** The massive slip caused a significant seafloor uplift (up to 50 meters in some areas), displacing millions of tons of water and triggering a massive tsunami.
        """)
        st.markdown('</div>', unsafe_allow_html=True)

elif selection == "3. Key Facts & Statistics":
    st.markdown('<p class="main-header">Key Facts</p>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Date", "11 March 2011")
    col2.metric("Magnitude", "9.0 Mw", "Strongest in Japan's history")
    col3.metric("Depth", "~30 km", "Relatively shallow")
    
    st.markdown("---")
    
    col4, col5 = st.columns(2)
    with col4:
        st.markdown("### Tsunami Characteristics")
        st.metric("Max Tsunami Wave Height", "Up to 40 metres")
        st.metric("Speed of Tsunami", "~800 km/h", "Similar to a commercial jet plane")
        
    with col5:
        # Comparison chart for Tsunami Height
        df_tsunami = pd.DataFrame({
            "Landmark/Wave": ["Average 2-story house", "2004 Indian Ocean Tsunami", "2011 Tohoku Tsunami"],
            "Height (Metres)": [6, 30, 40]
        })
        fig = px.bar(df_tsunami, x="Landmark/Wave", y="Height (Metres)", 
                     title="Tsunami Wave Height Comparison", 
                     color="Height (Metres)", color_continuous_scale="Blues")
        st.plotly_chart(fig, use_container_width=True)

elif selection == "4. Primary & Secondary Effects":
    st.markdown('<p class="main-header">Impact & Devastation</p>', unsafe_allow_html=True)
    
    tab1, tab2 = st.tabs(["Primary Effects (Immediate)", "Secondary Effects (Long-term/Triggered)"])
    
    with tab1:
        st.markdown("### Primary Effects of the Earthquake")
        st.markdown("""
        * **Casualties:** ~16,000 deaths and thousands injured.
        * **Infrastructure:** Buildings collapsed, and major road/railway networks were heavily damaged.
        * **Power:** Power outages affected millions of homes immediately.
        * **Hazards:** Fires broke out in urban areas due to ruptured gas lines.
        * **Transport:** Severe transport disruption, including the automatic halting of bullet trains.
        """)
        
    with tab2:
        st.markdown("### Secondary Effects (The Major Focus)")
        st.markdown("""
        * **Tsunami Devastation:** The tsunami devastated coastal areas, destroying entire towns (e.g., in the Sendai region).
        * **Nuclear Disaster:** Flooding led to the Fukushima Daiichi Nuclear Power Plant disaster, resulting in severe radiation leaks.
        * **Environmental:** Long-term environmental contamination of land and water due to radiation and debris.
        * **Displacement:** Over 500,000 people were displaced from their homes.
        """)
        
        # Economic loss chart
        st.markdown("#### Economic Loss Comparison")
        df_econ = pd.DataFrame({
            "Disaster": ["1995 Kobe Earthquake", "2004 Indian Ocean Tsunami", "2005 Hurricane Katrina", "2011 Tohoku Earthquake"],
            "Estimated Cost (Billion USD)": [100, 15, 125, 235]
        })
        fig2 = px.bar(df_econ, x="Disaster", y="Estimated Cost (Billion USD)", 
                      color="Estimated Cost (Billion USD)", color_continuous_scale="Reds",
                      title="Costliest Disasters in History")
        st.plotly_chart(fig2, use_container_width=True)

elif selection == "5. Responses (Immediate & Long-Term)":
    st.markdown('<p class="main-header">Disaster Response</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### Immediate Responses")
        st.success("""
        * **Early Warning Systems:** Advanced systems alerted citizens seconds before the violent shaking began, saving countless lives.
        * **Automation:** Bullet trains and factories shut down automatically upon detecting primary waves.
        * **Deployment:** 100,000+ Japanese Self-Defense Forces were deployed rapidly.
        * **Global Aid:** Massive international rescue and aid support arrived within days.
        * **Evacuation:** Immediate establishment of evacuation zones near the Fukushima nuclear plant.
        """)
        
    with col2:
        st.markdown("### Long-Term Responses")
        st.info("""
        * **Rebuilding:** Massive reconstruction of coastal towns and critical infrastructure.
        * **Defenses:** Construction of improved tsunami defenses, including significantly higher and deeper sea walls.
        * **Regulations:** Implementation of stricter nuclear safety regulations nationwide.
        * **Preparedness:** Enhanced disaster preparedness programs and regular drills for citizens.
        * **Relocation:** Permanent relocation of highly vulnerable coastal communities to higher ground.
        """)

elif selection == "6. Why Were Impacts So High?":
    st.markdown('<p class="main-header">Analysis: Why were the impacts so devastating?</p>', unsafe_allow_html=True)
    st.markdown("Despite Japan being one of the most developed and earthquake-prepared nations on Earth, the disaster resulted in massive loss of life and property. Here is why:")
    
    st.markdown('<div class="fact-box">', unsafe_allow_html=True)
    st.markdown("""
    1. **Extremely High Magnitude:** At 9.0 Mw, the earthquake was exponentially more powerful than what many older structures and sea walls were engineered to withstand.
    2. **The Powerful Tsunami:** The earthquake itself caused relatively few deaths; the primary cause of the mass fatalities was the sheer scale and speed of the tsunami.
    3. **Coastal Population Concentration:** Japan's mountainous interior means a vast majority of the population and industry (including power plants) are densely packed along vulnerable flat coastlines.
    4. **Nuclear Hazard Multiplier:** The flooding of the Fukushima Daiichi plant created a cascading disaster, vastly increasing the severity, economic loss, and long-term displacement of the event.
    """)
    st.markdown('</div>', unsafe_allow_html=True)
