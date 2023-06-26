import streamlit as st  # calls the module as an alias
import pandas as pd
import requests

st.set_page_config(
    page_title="AkashaGG - Streamlit Project",
    layout="wide",
    menu_items={
        'Get Help': 'https://docs.streamlit.io/',
        'About': '# Welcome to AkashaGG! Developed by Gabriel Gomez.',
    }
)

add_selectbox = st.sidebar.selectbox(
    "Select a Category:",
    ["Homepage", "Artifacts", "Characters", "Weapons (Coming Soon)", "Fun Stuff!"]
)

if add_selectbox == "Artifacts":  # If category selected is "Artifacts"
    st.title("Artifact Reliquary")
    st.subheader("Find basic information for artifact sets")

    reliquaryURL = "https://genshin-db-api.vercel.app/api/artifacts?query="  # Base URL for artifact queries
    reliquaryResponse = requests.get(reliquaryURL + "names&matchCategories=true").json()  # Returns all artifact names

    artifact = st.selectbox("Choose an artifact set:", options=reliquaryResponse)  # Displays all artifacts from API
    artifactResponse = requests.get(reliquaryURL + artifact).json()  # Query for user's selected artifact

    singleArtifacts = {"Prayers for Destiny", "Prayers for Illumination", "Prayers for Wisdom", "Prayers to Springtime"}

    # Check if selected artifact set is not a singular artifact (they have less attributes, which is important)
    if artifact not in singleArtifacts:
        # Artifact Attributes
        # Format: arti = artifactResponse[""]
        artiTwoPiece = artifactResponse["2pc"]
        artiFourPiece = artifactResponse["4pc"]
        artiFlower = artifactResponse["images"]["flower"]
        artiPlume = artifactResponse["images"]["plume"]
        artiSands = artifactResponse["images"]["sands"]
        artiGoblet = artifactResponse["images"]["goblet"]
        artiCirclet = artifactResponse["images"]["circlet"]

        st.write("**_2-Piece Set Bonus:_** " + artiTwoPiece)
        st.write("**_4-Piece Set Bonus:_** " + artiFourPiece)

        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            st.image("{}".format(artiFlower))
            st.caption("Flower of Life")

        with col2:
            st.image("{}".format(artiPlume))
            st.caption("Plume of Death")

        with col3:
            st.image("{}".format(artiSands))
            st.caption("Sands of Eon")

        with col4:
            st.image("{}".format(artiGoblet))
            st.caption("Goblet of Eonothem")

        with col5:
            st.image("{}".format(artiCirclet))
            st.caption("Circlet of Logos")

        st.write("--")

        st.subheader("Compare possible mainstats for each artifact piece below.")
        df = pd.DataFrame(
            [["Flat HP",
              "Flat ATK",
              "HP%, ATK%, DEF%, EM, ER%",
              "HP%, ATK%, DEF%, EM, DMG%",
              "HP%, ATK%, DEF%, EM, CR%, CD%, HB%"]],
            columns=[
                "Flower of Life",
                "Plume of Death",
                "Sands of Eon",
                "Goblet of Eonothem",
                "Circlet of Logos"
            ],
        )

        # CSS to inject contained in a string
        hide_table_row_index = """
                    <style>
                    thead tr th:first-child {display:none}
                    tbody th {display:none}
                    </style>
                    """
        st.markdown(hide_table_row_index, unsafe_allow_html=True) # Inject CSS with markdown to remove row indices

        st.table(df)

        st.write("--")

        with st.expander("See more details about artifact stats:"):
            st.write("- HP(%): Increases the Max HP stat of the equipping character.\n"
                     "\n- ATK(%): Increases the ATK stat of the equipping character.\n"
                     "\n- DEF(%): Increases the DEF stat of the equipping character.\n"
                     "\n- EM: Increases the Elemental Mastery stat of the equipping character.\n"
                     "\n- ER(%): Increases the Energy Recharge stat of the equipping character.\n"
                     "\n- DMG(%): Increases the Elemental or Physical Damage Bonus of the equipping character. "
                     "Elemental DMG% is specific to one of the following: Pyro, Cryo, Hydro, Electro, Anemo, Geo, "
                     "or Dendro.\n"
                     "\n- CR%: Increases the Crit Rate stat of the equipping character."
                     "\n- CD%: Increases the Crit DMG stat of the equipping character."
                     "\n- HB%: Increases the Healing Bonus stat of the equipping character.")

    else:  # If the selected artifact set is one of the singular sets, it has less attributes to display
        # Artifact Attributes
        # Format: arti = artifactResponse[""]
        artiOnePiece = artifactResponse["1pc"]
        artiCirclet = artifactResponse["images"]["circlet"]

        st.write("**_1-Piece Set Bonus:_** " + artiOnePiece)

        st.image("{}".format(artiCirclet))
        st.caption("Circlet of Logos")

        st.subheader("Compare possible mainstats for each artifact piece below.")
        parameters = st.multiselect(
            "Select One or More Artifact Pieces",
            ["Circlet of Logos"]
        )
        df = pd.DataFrame(
            [["HP%, ATK%, DEF%, EM, CR%, CD%, HB%"]],
            columns=["Circlet of Logos"],
        )

        if parameters:
            st.dataframe(df[parameters])

        st.write("--")

        with st.expander("See more details about artifact stats:"):
            st.write("- HP(%): Increases the Max HP stat of the equipping character.\n"
                     "\n- ATK(%): Increases the ATK stat of the equipping character.\n"
                     "\n- DEF(%): Increases the DEF stat of the equipping character.\n"
                     "\n- EM: Increases the Elemental Mastery stat of the equipping character.\n"
                     "\n- ER(%): Increases the Energy Recharge stat of the equipping character.\n"
                     "\n- DMG(%): Increases the Elemental or Physical Damage Bonus of the equipping character. "
                     "Elemental DMG% is specific to one of the following: Pyro, Cryo, Hydro, Electro, Anemo, Geo, "
                     "or Dendro.\n"
                     "\n- CR%: Increases the Crit Rate stat of the equipping character."
                     "\n- CD%: Increases the Crit DMG stat of the equipping character."
                     "\n- HB%: Increases the Healing Bonus stat of the equipping character.")

elif add_selectbox == "Characters":
    st.title("Character Archive")
    st.subheader("Find basic information for playable characters")
    st.warning("WARNING: New/unreleased characters may not be fully updated in the database.")

    archiveURL = "https://genshin-db-api.vercel.app/api/characters?query="  # Base URL for character queries
    archiveResponse = requests.get(archiveURL + "names&matchCategories=true").json()  # Returns all character names

    character = st.selectbox("Choose a character:", options=archiveResponse)  # Displays all character names from API
    characterResponse = requests.get(archiveURL + character).json()  # Query for user's selected character

    if character:
        # Character Attributes
        # Format: chara = characterResponse[""]
        charFullName = characterResponse["fullname"]
        charTitle = characterResponse["title"]
        charDesc = characterResponse["description"]
        charWeapon = characterResponse["weapontype"]
        charRarity = characterResponse["rarity"]
        charElement = characterResponse["element"]

        # Character Images
        charAvatar = characterResponse["images"]["icon"]
        charSideIcon = characterResponse["images"]["sideicon"]

        col1, col2, col3 = st.columns(3)

        with col1:
            st.image("{}".format(charAvatar))

        with col2:
            st.write("**_Name:_** " + charFullName)
            st.write("**_Rarity:_** " + charRarity + " Star")
            st.write("**_Description:_** " + charDesc)

        with col3:
            st.write("**_Weapon Type:_** " + charWeapon)
            st.write("**_Element:_** " + charElement)

elif add_selectbox == "Weapons (Coming Soon)":
    st.title("Weapons Armory")
    st.error("This area isn't quite ready to explore just yet!")
    st.write("**_Paimon_** : How about we explore the area ahead of us later?")
    agree = st.checkbox("Alright Paimon...")
    if agree:
        st.image("media/paimon_happy.png", width=200)
    else:
        st.image("media/paimon_shock.png", width=200)

elif add_selectbox == "Fun Stuff!":
    st.title("Fun Stuff!")

    st.subheader("Calculate your chances of getting a 5-star within a certain amount of wishes!")
    numPulls = st.slider(label="How many wishes will you use?", min_value=0, max_value=90)
    chanceFiveStar = 0.6 * numPulls
    if numPulls < 90:
        st.info("Your chances of getting a 5-star within " + str(numPulls) + " wishes is approximately: "
                + str(chanceFiveStar) + "%")
    else:
        st.info("A 5-star character is guaranteed within every 90 wishes due to the pity system.")

    st.write("--")

    st.subheader("This Streamlit webapp was created using genshin-db, documented on GitHub!")
    genshinDBurl = 'https://github.com/theBowja/genshin-db'
    if st.button('Woah, let me see!'):
        st.write("Sure! Here's the link:\n" + genshinDBurl)

    st.write("--")

    st.subheader("Genshin Impact is developed by miHoYo, a company based in Shanghai, China!")
    if st.select_slider(label="Map Toggle", options=["Don't Display Map", "Display Map"], value="Don't Display Map",
                        label_visibility="hidden") == "Display Map":
        map_data = pd.DataFrame({
            'Location': ['miHoYo Headquarters'],
            'lat': [31.16985883140126],
            'lon': [121.4305785400194]
        })
        st.map(map_data)

    st.write("--")

else:
    col1, col2 = st.columns(2)

    with col1:
        st.title("AkashaGG")
        st.subheader("A Genshin Impact project developed by Gabriel Gomez.")
        st.info("Select a category in the sidebar to get started!")

    with col2:
        st.image("media/akashagg_logo.png", width=250)
