import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="2011 Japan Earthquake Presentation", page_icon="🇯🇵", layout="wide")

# --- CUSTOM CSS FOR AESTHETICS ---
st.markdown("""
    <style>
    .main-title {font-size: 48px; font-weight: 800; color: #1E3A8A; margin-bottom: 0px; text-align: center;}
    .sub-title {font-size: 24px; color: #3B82F6; margin-bottom: 30px; text-align: center;}
    .card {background-color: #ffffff; padding: 25px; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); border-top: 5px solid #1E3A8A; margin-bottom: 20px;}
    .quote-box {background-color: #F3F4F6; padding: 20px; border-left: 5px solid #F59E0B; border-radius: 5px; font-style: italic; color: #374151;}
    h3 {color: #1E40AF;}
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
st.sidebar.image("https://upload.wikimedia.org/wikipedia/en/thumb/9/9e/Flag_of_Japan.svg/320px-Flag_of_Japan.svg.png", width=100)
st.sidebar.title("Navigation")
st.sidebar.markdown("Explore the 2011 Tohoku Earthquake & Tsunami Case Study.")

sections = [
    "1. Overview & Map 🌍",
    "2. The Science: Why it Happened 💥",
    "3. The Tsunami & Fukushima 🌊",
    "4. Human & Economic Toll 📉",
    "5. Lessons & Official Sources 📚"
]
selection = st.sidebar.radio("Go to slide:", sections)

st.sidebar.markdown("---")
st.sidebar.info("Built with Streamlit & Plotly\nData sourced from USGS, IAEA, JMA, and World Bank.")

# --- SLIDE 1: OVERVIEW & MAP ---
if selection == "1. Overview & Map 🌍":
    st.markdown('<p class="main-title">The 2011 Great East Japan Earthquake</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">A devastating 9.0 magnitude megaquake that altered history</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1.2])
    
    with col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### The Basics")
        st.markdown("""
        * **Date & Time:** March 11, 2011 at 2:46 PM (Local Time)
        * **Magnitude:** 9.0–9.1 Mw (Strongest ever recorded in Japan)
        * **Duration of Shaking:** Approximately 6 minutes
        * **Location:** Tohoku region (North-East Honshu)
        * **Epicenter:** 130 km east of Sendai in the Pacific Ocean
        """)
        
        st.markdown('<div class="quote-box">"This was a massive earthquake, one of the largest earthquakes that we have ever recorded during the past hundred years of instrumental studies." <br><br>— <b>Bill Ellsworth, U.S. Geological Survey (USGS)</b></div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        # Interactive Map showing Epicenter, Sendai, and Fukushima
        df_map = pd.DataFrame({
            "Location": ["Epicenter (Mag 9.0)", "Fukushima Daiichi Plant", "Sendai City (Devastated Area)"],
            "lat": [38.322, 37.421, 38.268],
            "lon": [142.369, 141.032, 140.871],
            "Category": ["Epicenter", "Nuclear Disaster", "Major City"]
        })
        
        fig = px.scatter_mapbox(
            df_map, lat="lat", lon="lon", color="Category", hover_name="Location",
            color_discrete_map={"Epicenter": "red", "Nuclear Disaster": "orange", "Major City": "blue"},
            zoom=5, height=500, mapbox_style="carto-positron", title="Key Locations of the Disaster"
        )
        fig.update_traces(marker=dict(size=16, symbol='circle'))
        st.plotly_chart(fig, use_container_width=True)

# --- SLIDE 2: THE SCIENCE ---
elif selection == "2. The Science: Why it Happened 💥":
    st.markdown('<p class="main-title">Geological Mechanics</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">Understanding Destructive Plate Boundaries</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### The Subduction Zone (Simple Explanation)")
        st.markdown("""
        Japan sits on the highly active "Ring of Fire". The earthquake was caused by a **convergent (destructive) plate boundary**:
        
        1. **The Plates:** The heavy Pacific Plate is continuously moving toward Japan.
        2. **The Subduction:** It gets forced *underneath* the lighter North American Plate (Okhotsk microplate).
        3. **The Snag:** The plates get stuck due to friction. Tension builds up for centuries.
        4. **The Snap:** On March 11, the rock finally gave way. The North American plate violently snapped upward.
        """)
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### Extreme Energy Release")
        st.metric(label="Energy Equivalent", value="600 Million x", delta="Hiroshima Bombs (Approx.)", delta_color="off")
        st.markdown("""
        The sheer force of this earthquake was so immense that it:
        * Shifted the main island of Honshu **2.4 meters to the east**.
        * Shifted the Earth on its axis by up to **25 centimeters**.
        * Sped up the Earth's rotation, making days **1.8 microseconds shorter**.
        """)
        st.markdown('</div>', unsafe_allow_html=True)

# --- SLIDE 3: TSUNAMI & FUKUSHIMA ---
elif selection == "3. The Tsunami & Fukushima 🌊":
    st.markdown('<p class="main-title">The Secondary Hazards</p>', unsafe_allow_html=True)
    
    tab1, tab2 = st.tabs(["🌊 The Tsunami", "☢️ Fukushima Daiichi Disaster"])
    
    with tab1:
        st.markdown("### A Wall of Water")
        st.write("When the tectonic plate snapped upward, it displaced millions of tons of ocean water, triggering a mega-tsunami.")
        
        col1, col2 = st.columns([1, 1])
        with col1:
            st.markdown("""
            * **Wave Height:** Up to 40 meters (133 ft) in some coastal towns like Miyako.
            * **Wave Speed:** Reached 700 km/h (435 mph) over the ocean—as fast as a jet plane.
            * **Inland Reach:** Water surged up to 10 km (6 miles) inland, completely flattening towns.
            """)
        with col2:
            df_wave = pd.DataFrame({
                "Object": ["Average Human", "2-Story House", "2004 Indian Ocean Tsunami", "2011 Tohoku Tsunami"],
                "Height (Meters)": [1.8, 6, 30, 40]
            })
            fig = px.bar(df_wave, x="Object", y="Height (Meters)", color="Height (Meters)", color_continuous_scale="Blues", title="Tsunami Height Comparison")
            st.plotly_chart(fig, use_container_width=True)
            
    with tab2:
        st.markdown("### Nuclear Emergency (Level 7 Incident)")
        st.write("The earthquake safely shut down the Fukushima reactors. However, the tsunami breached the 5.7-meter seawall, flooding the backup generators. Without power, the cooling systems failed, leading to meltdowns.")
        
        st.markdown('<div class="quote-box">"A major factor that contributed to the accident was the widespread assumption in Japan that its nuclear power plants were so safe that an accident of this magnitude was simply unthinkable." <br><br>— <b>International Atomic Energy Agency (IAEA) Report</b></div>', unsafe_allow_html=True)

# --- SLIDE 4: HUMAN & ECONOMIC TOLL ---
elif selection == "4. Human & Economic Toll 📉":
    st.markdown('<p class="main-title">The Aftermath</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Human Casualties")
        st.info("The vast majority of casualties were caused by drowning from the tsunami, not falling buildings, showcasing the effectiveness of Japan's earthquake-resistant engineering.")
        df_cas = pd.DataFrame({
            "Status": ["Confirmed Deaths", "Missing", "Injured"],
            "Count": [19759, 2553, 6242]
        })
        fig = px.pie(df_cas, values="Count", names="Status", hole=0.4, title="Casualty Breakdown (2021 Official Figures)", color_discrete_sequence=["#EF4444", "#F59E0B", "#3B82F6"])
        st.plotly_chart(fig, use_container_width=True)
        
    with col2:
        st.markdown("### The Most Expensive Disaster in History")
        st.markdown('<div class="quote-box">"The massive quake and tsunami of March 11 could cost Japan\'s economy up to $US235 billion... or 4.0 per cent of output." <br><br>— <b>World Bank (2011 Report)</b></div>', unsafe_allow_html=True)
        
        df_econ = pd.DataFrame({
            "Disaster Event": ["1995 Kobe Quake", "2005 Hurricane Katrina", "2011 Tohoku Quake & Tsunami"],
            "Estimated Cost (Billion USD)": [100, 125, 235]
        })
        fig2 = px.bar(df_econ, x="Disaster Event", y="Estimated Cost (Billion USD)", title="Economic Cost Comparison", color="Estimated Cost (Billion USD)", color_continuous_scale="Reds")
        st.plotly_chart(fig2, use_container_width=True)

# --- SLIDE 5: LESSONS & SOURCES ---
elif selection == "5. Lessons & Official Sources 📚":
    st.markdown('<p class="main-title">Lessons Learned & Official Sources</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### How Japan Responded")
        st.markdown("""
        * **Early Warning:** JMA's system sent alerts to millions of phones 15 seconds before the shaking began, saving countless lives.
        * **Infrastructure Updates:** Construction of massive new sea walls, some up to 12.5 meters high, across 400km of coastline.
        * **Nuclear Overhaul:** All nuclear plants were temporarily shut down; new, much stricter safety regulations were enforced globally.
        """)
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### Verify the Facts (Official Links)")
        
        # Using standard Markdown syntax for clickable links instead of HTML
        st.markdown("""
        To read the official scientific summaries and economic reports, visit the authoritative sources below:
        
        * 🌍 [US Geological Survey (USGS): Event Summary](https://www.usgs.gov/centers/pcmsc/news/japan-lashed-powerful-earthquake-devastating-tsunami)
        * ☢️ [IAEA: Fukushima Daiichi Accident Report](https://www.iaea.org/topics/response/fukushima-daiichi-nuclear-accident)
        * 💰 [World Bank: Economic Impact Estimate](https://www.worldbank.org/en/news/feature/2011/03/21/japan-earthquake)
        * 🌧️ [Japan Meteorological Agency (JMA) Portal](https://www.jma.go.jp/jma/en/2011_Earthquake/2011_Earthquake.html)
        """)
        
        st.markdown('</div>', unsafe_allow_html=True)
