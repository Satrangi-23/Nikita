# Set page config
st.set_page_config(
    page_title="Happy Birthday Nikita!",
    page_icon="🎂",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply custom CSS
st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    .stButton button {
        background-color: #FF4B4B;
        color: white;
        font-weight: bold;
        border-radius: 20px;
        padding: 10px 20px;
        border: none;
        transition: all 0.3s ease;
    }
    .stButton button:hover {
        background-color: #FF2E2E;
        transform: scale(1.05);
    }
    h1, h2, h3 {
        color: #FF4B4B;
        font-family: 'Comic Sans MS', cursive, sans-serif;
    }
    .birthday-card {
        background-color: white;
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }
    .confetti {
        position: fixed;
        width: 10px;
        height: 10px;
        background-color: #f2d74e;
        animation: confetti-fall 5s ease-in-out infinite;
    }
    @keyframes confetti-fall {
        0% {transform: translateY(-100vh) rotate(0deg);}
        100% {transform: translateY(100vh) rotate(720deg);}
    }
</style>
""", unsafe_allow_html=True)

# Create confetti effect
def create_confetti():
    confetti_html = ""
    colors = ["#f2d74e", "#95c3de", "#ff7096", "#9bdb4d", "#a980f1"]
    for i in range(100):
        size = random.randint(5, 10)
        left = random.randint(0, 100)
        animation_delay = random.uniform(0, 5)
        color = random.choice(colors)
        confetti_html += f"""
        <div class="confetti" style="left: {left}vw; width: {size}px; height: {size}px; 
        background-color: {color}; animation-delay: {animation_delay}s;"></div>
        """
    st.markdown(confetti_html, unsafe_allow_html=True)

# Sidebar for navigation and controls
st.sidebar.title("Birthday Menu 🎉")
page = st.sidebar.radio("Choose a section:", ["Home", "Photo Gallery", "Birthday Wishes", "Birthday Stats", "Memory Game", "Birthday Playlist"])

# Function to load uploaded images
def load_images():
    if 'uploaded_images' not in st.session_state:
        st.session_state.uploaded_images = []
    
    uploaded_files = st.file_uploader("Upload Nikita's photos", type=["jpg", "jpeg", "png"], accept_multiple_files=True)
    
    if uploaded_files:
        for file in uploaded_files:
            if file not in [img["file"] for img in st.session_state.uploaded_images]:
                img = Image.open(file)
                st.session_state.uploaded_images.append({
                    "file": file,
                    "image": img,
                    "caption": st.text_input(f"Caption for {file.name}", value="Happy Birthday Nikita!")
                })

# Home page
if page == "Home":
    create_confetti()
    
    st.markdown("<div class='birthday-card'>", unsafe_allow_html=True)
    st.title("🎉 Happy Birthday Nikita! 🎂")
    
    # Get current year
    current_year = datetime.now().year
    
    # Birthday message
    st.markdown(f"""
    <h2 style='text-align: center; margin-top: 20px;'>Wishing you the most amazing day!</h2>
    <p style='font-size: 22px; text-align: center;'>May your {current_year} be filled with love, laughter, and unforgettable moments.</p>
    """, unsafe_allow_html=True)
    
    # Birthday cake animation
    cake_cols = st.columns(3)
    with cake_cols[1]:
        st.markdown("""
        <div style='text-align: center;'>
            <div style='font-size: 100px; margin-bottom: 20px;'>
                🎂
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Birthday countdown
    st.subheader("Birthday Countdown:")
    countdown_placeholder = st.empty()
    
    for i in range(10, 0, -1):
        countdown_placeholder.markdown(f"<h1 style='text-align: center;'>{i}</h1>", unsafe_allow_html=True)
        time.sleep(0.3)
    
    countdown_placeholder.markdown("<h1 style='text-align: center; color: #FF4B4B;'>HAPPY BIRTHDAY!</h1>", unsafe_allow_html=True)
    
    # Birthday balloon animation
    balloon_cols = st.columns(7)
    for i, col in enumerate(balloon_cols):
        with col:
            st.markdown(f"""
            <div style='text-align: center; animation: float {i+2}s ease-in-out infinite alternate;'>
                <div style='font-size: 60px;'>
                    🎈
                </div>
            </div>
            <style>
                @keyframes float {{
                    0% {{transform: translateY(0px);}}
                    100% {{transform: translateY(-20px);}}
                }}
            </style>
            """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Interactive birthday message
    st.markdown("<div class='birthday-card'>", unsafe_allow_html=True)
    st.subheader("Customize your birthday message:")
    
    custom_name = st.text_input("Your Name:", "Friend")
    custom_message = st.text_area("Your Birthday Message:", "Wishing you all the happiness in the world!")
    
    if st.button("Generate Birthday Card"):
        st.success("Birthday message created successfully!")
        st.markdown(f"""
        <div style='background: linear-gradient(45deg, #ff9a9e 0%, #fad0c4 99%, #fad0c4 100%); padding: 30px; border-radius: 15px; text-align: center;'>
            <h2>Dear Nikita,</h2>
            <p style='font-size: 20px;'>{custom_message}</p>
            <p style='font-size: 18px; font-style: italic; margin-top: 30px;'>With love from,<br>{custom_name}</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

# Photo Gallery page
elif page == "Photo Gallery":
    st.markdown("<div class='birthday-card'>", unsafe_allow_html=True)
    st.title("📸 Nikita's Birthday Photo Gallery")
    st.write("Upload and view special photos of Nikita!")
    
    load_images()
    
    if st.session_state.uploaded_images:
        st.subheader("Photo Gallery")
        
        # Create a grid layout for images
        cols = st.columns(3)
        
        for i, img_data in enumerate(st.session_state.uploaded_images):
            with cols[i % 3]:
                st.image(img_data["image"], caption=img_data["caption"], use_column_width=True)
                
                # Add photo effects
                effect = st.selectbox(f"Effect for photo {i+1}", ["None", "Black & White", "Sepia", "Blur"], key=f"effect_{i}")
                
                if effect == "Black & White":
                    bw_img = img_data["image"].convert("L")
                    st.image(bw_img, caption=f"{img_data['caption']} (B&W)", use_column_width=True)
                elif effect == "Sepia":
                    sepia_img = img_data["image"].convert("L")
                    sepia_data = np.array(sepia_img)
                    sepia_data = np.stack([sepia_data * 1.2, sepia_data * 0.9, sepia_data * 0.7], axis=2)
                    sepia_data = np.clip(sepia_data, 0, 255).astype(np.uint8)
                    sepia_img = Image.fromarray(sepia_data)
                    st.image(sepia_img, caption=f"{img_data['caption']} (Sepia)", use_column_width=True)
                elif effect == "Blur":
                    from PIL import ImageFilter
                    blur_img = img_data["image"].filter(ImageFilter.GaussianBlur(radius=3))
                    st.image(blur_img, caption=f"{img_data['caption']} (Blur)", use_column_width=True)
    else:
        st.info("Upload some photos to start creating your gallery!")
        
        # Display sample placeholder
        cols = st.columns(3)
        with cols[0]:
            st.image("https://via.placeholder.com/300x300?text=Upload+Photos", caption="Coming soon...")
        with cols[1]:
            st.image("https://via.placeholder.com/300x300?text=Birthday+Memories", caption="Coming soon...")
        with cols[2]:
            st.image("https://via.placeholder.com/300x300?text=Nikita's+Gallery", caption="Coming soon...")
    
    st.markdown("</div>", unsafe_allow_html=True)

# Birthday Wishes page
elif page == "Birthday Wishes":
    st.markdown("<div class='birthday-card'>", unsafe_allow_html=True)
    st.title("💌 Birthday Wishes for Nikita")
    
    # Initialize wishes list in session state if not exist
    if 'wishes' not in st.session_state:
        st.session_state.wishes = []
    
    # Form to add new wishes
    with st.form("wish_form"):
        st.subheader("Add your birthday wish:")
        name = st.text_input("Your Name:")
        relationship = st.selectbox("Your Relationship:", ["Friend", "Family", "Colleague", "Other"])
        message = st.text_area("Your Birthday Message:")
        emoji = st.selectbox("Choose an emoji:", ["🎉", "❤️", "🎁", "🎂", "✨", "🌟", "🥳"])
        
        submit_button = st.form_submit_button("Send Birthday Wish")
        
        if submit_button and name and message:
            st.session_state.wishes.append({
                "name": name,
                "relationship": relationship,
                "message": message,
                "emoji": emoji,
                "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
            st.success("Birthday wish added successfully!")
    
    # Display all birthday wishes
    st.subheader("Birthday Wishes for Nikita:")
    
    if not st.session_state.wishes:
        st.info("No birthday wishes yet. Be the first to wish Nikita!")
    else:
        for i, wish in enumerate(st.session_state.wishes):
            with st.container():
                st.markdown(f"""
                <div style='background-color: #f8f9fa; padding: 15px; border-radius: 10px; margin-bottom: 10px;'>
                    <h4>{wish["emoji"]} From: {wish["name"]} ({wish["relationship"]})</h4>
                    <p style='font-style: italic;'>{wish["message"]}</p>
                    <small>Sent on: {wish["time"]}</small>
                </div>
                """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

# Birthday Stats page
elif page == "Birthday Stats":
    st.markdown("<div class='birthday-card'>", unsafe_allow_html=True)
    st.title("📊 Nikita's Birthday Stats")
    
    # Generate some fake birthday stats
    years = list(range(datetime.now().year - 5, datetime.now().year + 1))
    gifts = [random.randint(3, 15) for _ in years]
    wishes = [random.randint(10, 50) for _ in years]
    cake_size = [random.randint(1, 3) for _ in years]
    
    birthday_data = pd.DataFrame({
        "Year": years,
        "Gifts Received": gifts,
        "Birthday Wishes": wishes,
        "Cake Size (kg)": cake_size
    })
    
    # Display birthday trends
    st.subheader("Birthday Trends Over Years")
    
    # Create tabs for different charts
    stat_tabs = st.tabs(["Gifts", "Wishes", "Cake Size", "Summary"])
    
    with stat_tabs[0]:
        fig_gifts = px.bar(birthday_data, x="Year", y="Gifts Received", 
                         title="Number of Gifts Over Years",
                         color="Gifts Received",
                         color_continuous_scale="Reds")
        st.plotly_chart(fig_gifts, use_container_width=True)
    
    with stat_tabs[1]:
        fig_wishes = px.line(birthday_data, x="Year", y="Birthday Wishes",
                           title="Birthday Wishes Over Years",
                           markers=True,
                           color_discrete_sequence=["#FF4B4B"])
        st.plotly_chart(fig_wishes, use_container_width=True)
    
    with stat_tabs[2]:
        fig_cake = px.area(birthday_data, x="Year", y="Cake Size (kg)",
                          title="Birthday Cake Size Over Years",
                          color_discrete_sequence=["#FFC0CB"])
        st.plotly_chart(fig_cake, use_container_width=True)
    
    with stat_tabs[3]:
        st.subheader("Birthday Summary")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Total Gifts", f"{sum(gifts)}", f"+{gifts[-1] - gifts[-2]}")
        
        with col2:
            st.metric("Average Wishes", f"{round(sum(wishes)/len(wishes), 1)}", f"+{wishes[-1] - wishes[-2]}")
        
        with col3:
            st.metric("Biggest Cake", f"{max(cake_size)} kg", f"{cake_size[-1] - cake_size[-2]} kg")
    
    # Fun birthday facts
    st.subheader("Fun Birthday Facts")
    
    facts = [
        "People who celebrate birthdays live longer!",
        "The 'Happy Birthday' song is the most recognized song in the English language.",
        "The tradition of putting candles on birthday cakes dates back to Ancient Greece.",
        "The most expensive birthday party ever cost $27.2 million!",
        "The world record for the most candles on a birthday cake is 72,585!"
    ]
    
    fact = st.selectbox("Select a fun fact:", facts)
    st.info(fact)
    
    st.markdown("</div>", unsafe_allow_html=True)

# Memory Game page
elif page == "Memory Game":
    st.markdown("<div class='birthday-card'>", unsafe_allow_html=True)
    st.title("🎮 Birthday Memory Game")
    st.write("Test your memory with this fun birthday-themed game!")
    
    # Initialize game state
    if 'memory_board' not in st.session_state:
        emojis = ["🎁", "🎂", "🎈", "🎉", "🎊", "🎀", "🧁", "🍰"]
        # Create pairs
        memory_emojis = emojis * 2
        random.shuffle(memory_emojis)
        st.session_state.memory_board = memory_emojis
        st.session_state.flipped = [False] * 16
        st.session_state.matched = [False] * 16
        st.session_state.first_selection = None
        st.session_state.moves = 0
        st.session_state.matches = 0
    
    # Handle game reset
    if st.button("Start New Game"):
        emojis = ["🎁", "🎂", "🎈", "🎉", "🎊", "🎀", "🧁", "🍰"]
        memory_emojis = emojis * 2
        random.shuffle(memory_emojis)
        st.session_state.memory_board = memory_emojis
        st.session_state.flipped = [False] * 16
        st.session_state.matched = [False] * 16
        st.session_state.first_selection = None
        st.session_state.moves = 0
        st.session_state.matches = 0
    
    # Display game metrics
    metrics_cols = st.columns(2)
    with metrics_cols[0]:
        st.metric("Moves", st.session_state.moves)
    with metrics_cols[1]:
        st.metric("Matches", f"{st.session_state.matches}/8")
    
    # Display memory board
    board_cols = st.columns(4)
    for i in range(16):
        col_idx = i % 4
        with board_cols[col_idx]:
            # Show card content or back
            if st.session_state.matched[i]:
                # Matched cards
                st.button(
                    st.session_state.memory_board[i], 
                    key=f"btn_{i}",
                    disabled=True,
                    help="Matched!"
                )
            elif st.session_state.flipped[i]:
                # Currently flipped card
                if st.button(
                    st.session_state.memory_board[i], 
                    key=f"btn_{i}",
                    help="Currently flipped"
                ):
                    pass  # Already flipped
            else:
                # Face down card
                if st.button("❓", key=f"btn_{i}", help="Click to flip"):
                    # Handle card flip logic
                    st.session_state.flipped[i] = True
                    
                    if st.session_state.first_selection is None:
                        # First card in a pair
                        st.session_state.first_selection = i
                    else:
                        # Second card in a pair
                        first_idx = st.session_state.first_selection
                        
                        # Increment moves
                        st.session_state.moves += 1
                        
                        # Check if match
                        if st.session_state.memory_board[first_idx] == st.session_state.memory_board[i]:
                            # Match found
                            st.session_state.matched[first_idx] = True
                            st.session_state.matched[i] = True
                            st.session_state.matches += 1
                        else:
                            # No match, flip back after a delay
                            st.session_state.flipped[first_idx] = False
                            st.session_state.flipped[i] = False
                        
                        # Reset first selection
                        st.session_state.first_selection = None
                    
                    # Rerun to update the UI
                    st.experimental_rerun()
    
    # Check for game completion
    if st.session_state.matches == 8:
        st.success(f"🎉 Congratulations! You completed the game in {st.session_state.moves} moves!")
        st.balloons()
    
    st.markdown("</div>", unsafe_allow_html=True)

# Birthday Playlist page
elif page == "Birthday Playlist":
    st.markdown("<div class='birthday-card'>", unsafe_allow_html=True)
    st.title("🎵 Nikita's Birthday Playlist")
    st.write("Create the perfect birthday playlist for Nikita!")
    
    # Initialize playlist in session state
    if 'playlist' not in st.session_state:
        st.session_state.playlist = [
            {"title": "Happy Birthday", "artist": "Traditional", "duration": "0:30"},
            {"title": "Celebration", "artist": "Kool & The Gang", "duration": "3:40"},
            {"title": "Birthday", "artist": "The Beatles", "duration": "2:42"}
        ]
    
    # Add new song to playlist
    with st.form("add_song"):
        st.subheader("Add a Song to Nikita's Birthday Playlist")
        song_title = st.text_input("Song Title:")
        song_artist = st.text_input("Artist:")
        song_duration = st.text_input("Duration (e.g. 3:45):")
        
        if st.form_submit_button("Add Song"):
            if song_title and song_artist and song_duration:
                st.session_state.playlist.append({
                    "title": song_title,
                    "artist": song_artist,
                    "duration": song_duration
                })
                st.success(f"Added '{song_title}' to the playlist!")
    
    # Display current playlist
    st.subheader("Current Playlist")
    
    for i, song in enumerate(st.session_state.playlist):
        with st.container():
            cols = st.columns([1, 3, 2, 2])
            with cols[0]:
                st.write(f"#{i+1}")
            with cols[1]:
                st.write(f"**{song['title']}**")
            with cols[2]:
                st.write(song['artist'])
            with cols[3]:
                st.write(song['duration'])
    
    # Calculate total playlist duration
    def parse_duration(duration_str):
        parts = duration_str.split(":")
        if len(parts) == 2:
            return int(parts[0]) * 60 + int(parts[1])
        elif len(parts) == 3:
            return int(parts[0]) * 3600 + int(parts[1]) * 60 + int(parts[2])
        return 0
    
    total_seconds = sum(parse_duration(song["duration"]) for song in st.session_state.playlist)
    hours, remainder = divmod(total_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    if hours > 0:
        playlist_duration = f"{hours}:{minutes:02d}:{seconds:02d}"
    else:
        playlist_duration = f"{minutes}:{seconds:02d}"
    
    st.info(f"Total playlist duration: {playlist_duration}")
    
    # Playlist recommendations
    st.subheader("Song Recommendations")
    
    birthday_songs = [
        {"title": "Birthday", "artist": "Katy Perry", "genre": "Pop"},
        {"title": "In Da Club", "artist": "50 Cent", "genre": "Hip Hop"},
        {"title": "It's My Party", "artist": "Lesley Gore", "genre": "Pop"},
        {"title": "Happy", "artist": "Pharrell Williams", "genre": "Pop"},
        {"title": "Celebration", "artist": "Kool & The Gang", "genre": "Funk"},
        {"title": "Birthday Cake", "artist": "Rihanna", "genre": "R&B"}
    ]
    
    genre_filter = st.multiselect("Filter by genre:", ["Pop", "Hip Hop", "R&B", "Funk", "Rock"])
    
    filtered_songs = birthday_songs
    if genre_filter:
        filtered_songs = [song for song in birthday_songs if song["genre"] in genre_filter]
    
    for song in filtered_songs:
        with st.container():
            cols = st.columns([3, 2, 1])
            with cols[0]:
                st.write(f"**{song['title']}**")
            with cols[1]:
                st.write(song['artist'])
            with cols[2]:
                st.write(song['genre'])
    
    st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("""
<div style="text-align: center; margin-top: 30px; padding: 20px; background-color: #f8f9fa; border-radius: 10px;">
    <p>Created with ❤️ for Nikita's Birthday</p>
    <p style="font-size: 12px;">© 2025 Birthday App Creator</p>
</div>
""", unsafe_allow_html=True)
