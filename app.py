import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit.components.v1 as components

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="2011 Japan Earthquake Presentation", page_icon="🇯🇵", layout="wide")

# --- SECTIONS DEFINITION ---
sections = [
    "1. Overview & Map 🌍",
    "2. The Science: Why it Happened 💥",
    "3. The Tsunami & Fukushima 🌊",
    "4. Toll & Aftermath 📉🏚️",
    "5. Lessons & Official Sources 📚",
    "6. Fun Facts & Trivia 🧠",
    "7. Test Your Knowledge (Quiz) 📝",
    "8. Summary & Key Takeaways 📌"
]

# --- STATE MANAGEMENT & NAVIGATION ---
if "slide_index" not in st.session_state:
    st.session_state.slide_index = 0
if "slide_counter" not in st.session_state:
    st.session_state.slide_counter = 0

def change_slide(new_index):
    if 0 <= new_index < len(sections) and new_index != st.session_state.slide_index:
        st.session_state.slide_index = new_index
        st.session_state.slide_counter += 1  # This counter is the magic key

def nav_next():
    change_slide(st.session_state.slide_index + 1)

def nav_prev():
    change_slide(st.session_state.slide_index - 1)

def on_sidebar_change():
    selected_name = st.session_state.sidebar_radio
    new_idx = sections.index(selected_name)
    change_slide(new_idx)

# --- SIDEBAR NAVIGATION ---
st.sidebar.image("https://raw.githubusercontent.com/lipis/flag-icons/main/flags/4x3/jp.svg", width=100)
st.sidebar.title("Navigation")
st.sidebar.markdown("Explore the 2011 Tohoku Earthquake & Tsunami Case Study.")

st.sidebar.radio(
    "Go to slide:", 
    sections, 
    index=st.session_state.slide_index, 
    key="sidebar_radio", 
    on_change=on_sidebar_change
)

selection = sections[st.session_state.slide_index]

st.sidebar.markdown("---")
st.sidebar.info("Built with Streamlit & Plotly\nData sourced from USGS, IAEA, JMA, and World Bank.")

# --- TSUNAMI WAVE & BULLETPROOF SCROLL LOCK ---
# We use slide_counter to guarantee the CSS and JS are completely rebuilt every click
current_counter = st.session_state.slide_counter

# 1. CSS Animation (Unique class forces replay)
st.markdown(f"""
    <style>
    @keyframes sweep-{current_counter} {{
        0% {{ transform: translateX(0); opacity: 1; }}
        80% {{ opacity: 1; }}
        100% {{ transform: translateX(250vw); opacity: 0; display: none; }}
    }}
    .wave-{current_counter} {{
        position: fixed;
        top: 0;
        left: -120vw;
        width: 120vw;
        height: 100vh;
        background: linear-gradient(90deg, transparent 0%, #1E3A8A 30%, #3B82F6 70%, #93C5FD 100%);
        z-index: 999999;
        pointer-events: none;
        border-top-right-radius: 50% 100%;
        border-bottom-right-radius: 50% 100%;
        animation: sweep-{current_counter} 1.2s cubic-bezier(0.25, 1, 0.5, 1) forwards;
    }}
    </style>
    <div class="wave-{current_counter}"></div>
""", unsafe_allow_html=True)

# 2. JavaScript Scroll Lock (Unique 'key' forces Streamlit to execute the script every time)
components.html("""
    <script>
        const doc = window.parent.document;
        
        // Remove focus from the clicked button immediately
        if (doc.activeElement) {
            doc.activeElement.blur();
        }
        
        function forceTop() {
            const containers = [
                doc.documentElement,
                doc.body,
                doc.querySelector('.main'),
                doc.querySelector('[data-testid="stAppViewContainer"]'),
                doc.querySelector('[data-testid="stMainBlockContainer"]')
            ];
            
            containers.forEach(el => {
                if (el) el.scrollTop = 0;
            });
            window.parent.scrollTo(0, 0);
        }
        
        // Fire repeatedly for 2 full seconds. 
        // This easily covers the time it takes for heavy Plotly charts to load.
        let ticks = 0;
        const scrollLock = setInterval(() => {
            forceTop();
            ticks++;
            if (ticks > 100) { // 100 ticks * 20ms = 2000ms (2 seconds)
                clearInterval(scrollLock);
            }
        }, 20);
    </script>
""", height=0, width=0, key=f"scroll_fix_{current_counter}")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    /* Safely apply STXingkai font ONLY to text elements */
    h1, h2, h3, h4, h5, h6, p, li, label, .main-title, .sub-title, .card, .quote-box {
        font-family: 'STXingkai', cursive, sans-serif !important;
    }

    /* Blue Bubble Style for Page Headings */
    .main-title {
        font-size: 42px; 
        font-weight: 800; 
        color: #ffffff !important; 
        background: linear-gradient(135deg, #60A5FA, #2563EB); 
        padding: 15px 35px;
        border-radius: 50px; 
        text-align: center;
        margin: 10px auto 20px auto;
        box-shadow: 0 8px 16px rgba(37, 99, 235, 0.3);
        border: 3px solid #BFDBFE;
        display: block;
    }
    
    .sub-title {
        font-size: 24px; 
        color: #1E40AF; 
        margin-bottom: 30px; 
        text-align: center;
        font-weight: bold;
    }
    
    .card {
        background-color: #ffffff; 
        padding: 25px; 
        border-radius: 12px; 
        box-shadow: 0 4px 6px rgba(0,0,0,0.1); 
        border-top: 5px solid #1E3A8A; 
        margin-bottom: 20px;
    }
    
    .quote-box {
        background-color: #F3F4F6; 
        padding: 20px; 
        border-left: 5px solid #F59E0B; 
        border-radius: 5px; 
        font-style: italic; 
        color: #374151;
    }
    
    h3 {
        color: #1E40AF;
    }
    
    /* Pin the popover containers behind the left sidebar with stealth hover behavior */
    div[data-testid="stElementContainer"]:has(div[data-testid="stPopover"]) {
        position: fixed !important;
        left: 10px !important;
        z-index: 9999 !important;
        opacity: 0.3;
        transition: opacity 0.3s ease;
    }
    
    div[data-testid="stElementContainer"]:has(div[data-testid="stPopover"]):hover {
        opacity: 1;
    }

    div[data-testid="stElementContainer"]:has(div[data-testid="stPopover"]):nth-of-type(1) { top: 80px !important; }
    div[data-testid="stElementContainer"]:has(div[data-testid="stPopover"]):nth-of-type(2) { top: 110px !important; }
    div[data-testid="stElementContainer"]:has(div[data-testid="stPopover"]):nth-of-type(3) { top: 140px !important; }

    div[data-testid="stPopover"] button {
        width: 20px !important;
        height: 20px !important;
        min-width: 20px !important;
        min-height: 20px !important;
        padding: 0px !important;
        border-radius: 0px !important; 
        background-color: #9CA3AF !important; 
        border: none !important;
    }
    
    div[data-testid="stPopover"] button p, 
    div[data-testid="stPopover"] button div {
        display: none !important;
    }
    </style>
""", unsafe_allow_html=True)


# --- SLIDE 1: OVERVIEW & MAP ---
if selection == "1. Overview & Map 🌍":
    st.markdown('<div class="main-title">The 2011 Great East Japan Earthquake</div>', unsafe_allow_html=True)
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
    st.markdown('<div class="main-title">Geological Mechanics</div>', unsafe_allow_html=True)
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
    st.markdown('<div class="main-title">The Secondary Hazards</div>', unsafe_allow_html=True)
    
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

# --- SLIDE 4: TOLL & AFTERMATH ---
elif selection == "4. Toll & Aftermath 📉🏚️":
    st.markdown('<div class="main-title">Toll & Long-Term Aftermath</div>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">Analyzing the immediate devastation and the decade-long legacy</p>', unsafe_allow_html=True)
    
    tab1, tab2, tab3, tab4 = st.tabs(["📉 Immediate Toll", "☢️ Environmental Legacy", "👥 Societal & Human Impact", "🏭 Global Economy"])
    
    with tab1:
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

    with tab2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### The Fukushima Clean-up")
        st.markdown("""
        * **Decommissioning:** Dismantling the melted Fukushima Daiichi reactors is expected to take **30 to 40 years**. Heavily shielded robots are still being used to map and retrieve highly radioactive fuel debris.
        * **Radioactive Water Release:** As of 2023, Japan began releasing over 1 million tons of treated, diluted radioactive wastewater into the Pacific Ocean. While approved by the UN's IAEA, it caused massive diplomatic fallout and seafood import bans from neighboring countries.
        * **Exclusion Zones:** Though heavily reduced over the last decade, large swathes of land around the plant remain uninhabitable "difficult-to-return" zones due to lingering soil radiation.
        """)
        st.markdown('</div>', unsafe_allow_html=True)

    with tab3:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### The Invisible Toll: Displacement & Trauma")
        st.markdown("""
        * **Displacement:** Over **470,000 people** were evacuated in the immediate aftermath. Even a decade later, tens of thousands remained unable or unwilling to return to their hometowns.
        * **Disaster-Related Deaths:** In Fukushima prefecture, the number of people who died from "disaster-related causes" (such as suicide, stress-induced illnesses, and poor living conditions during evacuation) actually **surpassed** the number of people killed directly by the earthquake and tsunami.
        * **Ghost Towns:** Many coastal towns have struggled to recover their populations, leaving behind aging demographics in newly built, but empty, infrastructure.
        """)
        st.markdown('</div>', unsafe_allow_html=True)

    with tab4:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### The Energy Shift & Supply Chain Shock")
        st.markdown("""
        * **The Global Supply Chain:** The Tohoku region was a major hub for automotive and electronics manufacturing. The disaster halted global production lines for companies like Toyota, Honda, and Apple due to a sudden lack of critical microchips, pigments, and auto parts.
        * **Japan's Energy Crisis:** Before 2011, nuclear power provided about **30% of Japan's electricity**. Following the disaster, Japan shut down all of its nuclear reactors. To keep the lights on, the country had to massively increase its imports of fossil fuels (coal and liquid natural gas), causing a severe trade deficit and a spike in carbon emissions.
        * **Reconstruction Budget:** The Japanese government allocated over **32 trillion yen** (approx. $250+ billion USD) for a massive "Build Back Better" reconstruction framework over 10 years.
        """)
        st.markdown('</div>', unsafe_allow_html=True)

# --- SLIDE 5: LESSONS & SOURCES ---
elif selection == "5. Lessons & Official Sources 📚":
    st.markdown('<div class="main-title">Lessons Learned & Official Sources</div>', unsafe_allow_html=True)
    
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
        
        st.markdown("""
        To read the official scientific summaries and economic reports, visit the authoritative sources below:
        
        * 🌍 [US Geological Survey (USGS): Event Summary](https://www.usgs.gov/centers/pcmsc/news/japan-lashed-powerful-earthquake-devastating-tsunami)
        * ☢️ [IAEA: Fukushima Daiichi Accident Report](https://www.iaea.org/topics/response/fukushima-daiichi-nuclear-accident)
        * 💰 [World Bank: Economic Impact Estimate](https://www.worldbank.org/en/news/feature/2011/03/21/japan-earthquake)
        * 🌧️ [Japan Meteorological Agency (JMA) Portal](https://www.jma.go.jp/jma/en/2011_Earthquake/2011_Earthquake.html)
        """)
        
        st.markdown('</div>', unsafe_allow_html=True)

# --- SLIDE 6: FUN FACTS & TRIVIA ---
elif selection == "6. Fun Facts & Trivia 🧠":
    st.markdown('<div class="main-title">Mind-Blowing Facts & Trivia</div>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">Fascinating and bizarre scientific realities of the 2011 disaster</p>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### 🌍 Shifting Planet Earth")
        st.markdown("""
        * **Axis Tilt:** The sheer release of tectonic energy shifted the planet's axis by roughly **10 to 25 centimeters** (4 to 10 inches).
        * **Shorter Days:** Because the Earth's mass shifted closer to its center during the fault slip, our rotation sped up slightly, making days **1.8 microseconds shorter** permanently!
        * **Islands on the Move:** The main island of Honshu was shoved eastward by about **2.4 meters (8 feet)** toward North America.
        """)
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### 🌊 Trans-Pacific Travelers")
        st.markdown("""
        * **Ghost Docks:** Entire concrete floating docks from Japanese fishing ports were ripped away and eventually drifted all the way across the Pacific Ocean, washing up on the beaches of Oregon, Washington, and California years later.
        * **Surviving Sea Life:** Some living Japanese coastal marine species (like fish and crabs) managed to survive a 5,000-mile, multi-year voyage across the ocean trapped inside these floating debris fragments.
        """)
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### ⚡ Breaking the Scale")
        st.markdown("""
        * **Seismograph Overload:** The earthquake was so violently powerful that it actually **maxed out standard seismographs** in Japan. Scientists had to rely on GPS data and distant global monitoring networks to accurately calculate its 9.0 magnitude.
        * **Jet Speed Tsunami:** The resulting tsunami waves traveled across the open ocean at speeds around **700 to 800 km/h (435 to 500 mph)**—matching the cruising speed of a modern commercial airliner.
        """)
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown("### 🔔 Ring of Fire Giants")
        st.markdown("""
        * **Megaquake Club:** The 2011 Tohoku earthquake ranks as the **4th largest earthquake** ever recorded globally since modern instrumental record-keeping began in 1900 (behind Chile 1960, Alaska 1964, and Sumatra 2004).
        * **Centuries of Silence:** GPS data revealed that the fault line where the quake happened had been locked and accumulating tension for **over 600 years** before it violently gave way.
        """)
        st.markdown('</div>', unsafe_allow_html=True)

# --- SLIDE 7: QUIZ ---
elif selection == "7. Test Your Knowledge (Quiz) 📝":
    st.markdown('<div class="main-title">Interactive Quiz</div>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">Test what you learned about the 2011 Tohoku Earthquake & Tsunami</p>', unsafe_allow_html=True)
    
    with st.form("quiz_form"):
        st.markdown("### Question 1: What was the magnitude of the Tohoku earthquake on the Moment Magnitude Scale?")
        q1 = st.radio("Select one:", ["7.5", "8.2", "9.0", "9.9"], key="q1", index=None)
        
        st.markdown("### Question 2: What was the primary cause of the vast majority of fatalities during the event?")
        q2 = st.radio("Select one:", ["Building collapses", "The massive Tsunami", "Fukushima radiation leaks", "Urban fires"], key="q2", index=None)
        
        st.markdown("### Question 3: Which two tectonic plates interacted at this subduction zone boundary?")
        q3 = st.radio("Select one:", ["Pacific Plate and North American Plate", "Eurasian Plate and African Plate", "Nazca Plate and South American Plate", "Indo-Australian Plate and Eurasian Plate"], key="q3", index=None)
        
        st.markdown("### Question 4: Approximately how much did the disaster cost in economic losses, making it the costliest natural disaster in history?")
        q4 = st.radio("Select one:", ["$50 billion", "$100 billion", "$235 billion", "$500 billion"], key="q4", index=None)
        
        submitted = st.form_submit_button("Submit Answers")
        
        if submitted:
            score = 0
            total = 4
            if q1 == "9.0": score += 1
            if q2 == "The massive Tsunami": score += 1
            if q3 == "Pacific Plate and North American Plate": score += 1
            if q4 == "$235 billion": score += 1
            
            st.markdown("---")
            st.subheader(f"Your Score: {score} / {total} ({int((score/total)*100)}%)")
            if score == total:
                st.success("🎉 Perfect score! You're an expert on the 2011 Tohoku disaster.")
            elif score >= 2:
                st.info("👍 Good job! Review the slides to brush up on what you missed.")
            else:
                st.warning("⚠️ Keep studying! Check out the overview and science slides to learn more.")

# --- SLIDE 8: SUMMARY & KEY TAKEAWAYS ---
elif selection == "8. Summary & Key Takeaways 📌":
    st.markdown('<div class="main-title">Summary & Key Takeaways</div>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">A quick executive recap of the 2011 Tohoku Earthquake & Tsunami</p>', unsafe_allow_html=True)
    
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("""
    ### 🔑 Core Summary Points
    
    1. **The Event:** On March 11, 2011, a **9.0 magnitude** megaquake struck off the coast of Sendai, Japan, resulting from the subduction of the Pacific Plate beneath the North American Plate.
    2. **The Main Hazard:** While the earthquake's engineering standards protected buildings from collapsing, the **40-meter tsunami wave** triggered by seafloor uplift caused the vast majority of the ~19,000 fatalities.
    3. **The Cascading Disaster:** Flooding of the backup generators at the **Fukushima Daiichi Nuclear Power Plant** caused a Level 7 nuclear meltdown, massive long-term displacement, and international fallout.
    4. **Economic & Global Impact:** Costing roughly **$235 billion**, it became the costliest natural disaster in history, sending supply chain shocks across global electronics and automotive industries.
    5. **Resilience & Adaptation:** Despite the unprecedented devastation, Japan's advanced early warning systems saved thousands of lives. The country responded with aggressive rebuilding frameworks, much higher sea walls, and global regulatory overhauls for nuclear safety.
    """)
    st.markdown('</div>', unsafe_allow_html=True)


# --- BOTTOM PPT-STYLE NAVIGATION BUTTONS ---
st.markdown("---")
col_prev, col_space, col_next = st.columns([2, 6, 2])

with col_prev:
    if st.session_state.slide_index > 0:
        st.button("◀ Previous Slide", on_click=nav_prev, type="primary", use_container_width=True)

with col_next:
    if st.session_state.slide_index < len(sections) - 1:
        st.button("Next Slide ▶", on_click=nav_next, type="primary", use_container_width=True)


# --- EASTER EGG POPOVERS (HIDDEN BEHIND LEFT SIDEBAR) ---

egg_top = st.popover("")
with egg_top:
    st.write("Authorized Access Only")
    code_top = st.text_input("Enter code:", type="password", key="egg_code_top")
    if code_top == "100%":
        st.success("Access Granted.")
        st.markdown("<h4 style='text-align:center;'>Hitler's Art School Application (1907)</h4>", unsafe_allow_html=True)
        df_art = pd.DataFrame({"Decision": ["Rejected", "Also Rejected, but in German", "Told to try Architecture instead"], "Percent": [70, 29, 1]})
        fig_art = px.pie(df_art, values="Percent", names="Decision", hole=0.3, color_discrete_sequence=px.colors.sequential.Reds_r)
        fig_art.update_layout(showlegend=False, margin=dict(l=0, r=0, t=30, b=0), height=250)
        st.plotly_chart(fig_art, use_container_width=True)
    elif code_top:
        st.error("Invalid Code.")

egg_mid = st.popover("")
with egg_mid:
    st.write("Authorized Access Only")
    code_mid = st.text_input("Enter code:", type="password", key="egg_code_mid")
    if code_mid == "100%":
        st.success("Access Granted.")
        st.markdown("<h4 style='text-align:center;'>Historically Nuked Countries</h4>", unsafe_allow_html=True)
        df_nuked = pd.DataFrame({"Country": ["Japan"], "Percentage": [100]})
        fig_egg = px.pie(df_nuked, values="Percentage", names="Country", color_discrete_sequence=["#BC002D"]) 
        fig_egg.update_layout(paper_bgcolor="white", plot_bgcolor="white", showlegend=False, margin=dict(l=0, r=0, t=0, b=0), height=200, width=200)
        fig_egg.update_traces(textinfo='none', hovertemplate='<b>%{label}</b><br>100%<extra></extra>')
        st.plotly_chart(fig_egg, use_container_width=True)
    elif code_mid:
        st.error("Invalid Code.")

egg_bot = st.popover("")
with egg_bot:
    st.write("Authorized Access Only")
    code_bot = st.text_input("Enter code:", type="password", key="egg_code_bot")
    if code_bot == "100%":
        st.success("Access Granted.")
        st.markdown("<h4 style='text-align:center;'>Success Rate: Invading Russia During Winter</h4>", unsafe_allow_html=True)
        df_inv = pd.DataFrame({"Dictator/General": ["Napoleon (1812)", "Hitler (1941)"], "Success Rate (%)": [0, 0]})
        fig_inv = px.bar(df_inv, x="Dictator/General", y="Success Rate (%)", range_y=[0, 100], color="Dictator/General", color_discrete_sequence=["#3B82F6", "#EF4444"])
        fig_inv.update_layout(showlegend=False, margin=dict(l=0, r=0, t=30, b=0), height=250)
        st.plotly_chart(fig_inv, use_container_width=True)
    elif code_bot:
        st.error("Invalid Code.")
