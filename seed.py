from app import db, Movie, Booking, app

with app.app_context():
    # Completely rebuild all tables in correct order
    db.drop_all()
    db.create_all()

    # ---------- MOVIE LIST ----------
    sample_movies = [
        Movie(
            title="Mahavatar Narsimha",
            description="Mythological Action Drama with powerful visuals.",
            genre="Action",
            image="static//Assests//Mahavatar-Narsimha.jpg",
            show_time="10:00 AM",
            screen="Screen 1"
        ),
        Movie(
            title="Saiyaara",
            description="A romantic musical journey filled with emotion.",
            genre="Romance",
            image="static//Assests//Saiyaara.jpg",
            show_time="12:30 PM",
            screen="Screen 2"
        ),
        Movie(
            title="Coolie",
            description="Comedy family entertainer full of fun and laughter.",
            genre="Comedy",
            image="static//Assests//Coolie.jpg",
            show_time="3:00 PM",
            screen="Screen 3"
        ),
        Movie(
            title="War 2",
            description="High-octane action thriller featuring elite agents.",
            genre="Action",
            image="static//Assests//War-2.jpg",
            show_time="6:00 PM",
            screen="Screen 1"
        ),
        Movie(
            title="Vash 2",
            description="A supernatural thriller that blurs the line between reality and fear.",
            genre="Thriller",
            image="static//Assests//Vash-2.jpg",
            show_time="8:45 PM",
            screen="Screen 2"
        ),
        Movie(
            title="The Fantastic Four",
            description="Four superheroes reunite to face an intergalactic threat.",
            genre="Sci-Fi",
            image="static//Assests//The Fantastic Four.jpg",
            show_time="10:00 AM",
            screen="Screen 3"
        ),
        Movie(
            title="Param Sundari",
            description="A glamorous musical full of dance and romance.",
            genre="Musical",
            image="static//Assests//Param Sundari.jpg",
            show_time="1:00 PM",
            screen="Screen 1"
        ),
        Movie(
            title="Son of Sardar 2",
            description="An action-comedy packed with Punjabi energy and chaos.",
            genre="Action-Comedy",
            image="static//Assests//Son of Sardar 2.jpg",
            show_time="4:00 PM",
            screen="Screen 2"
        ),
        Movie(
            title="Kalki 2898 AD",
            description="Epic sci-fi mythology with futuristic visuals and divine themes.",
            genre="Sci-Fi",
            image="static//Assests//Kalki 2898 AD.jpg",
            show_time="6:00 PM",
            screen="Screen 1"
        ),
        Movie(
            title="Jawan",
            description="High-octane thriller led by an unstoppable hero.",
            genre="Action",
            image="static//Assests//Jawan.jpg",
            show_time="8:45 PM",
            screen="Screen 2"
        ),
        Movie(
            title="Pathaan",
            description="Spy action blockbuster with global stakes.",
            genre="Action",
            image="static//Assests//pathaan.jpg",
            show_time="10:00 AM",
            screen="Screen 3"
        ),
        Movie(
            title="RRR",
            description="Freedom fighters and brotherhood with epic storytelling.",
            genre="Action",
            image="static//Assests//RRR.jpg",
            show_time="1:00 PM",
            screen="Screen 1"
        ),
        Movie(
            title="3 Idiots",
            description="College, friendship, and dreams that inspire a generation.",
            genre="Drama",
            image="static//Assests//3-Idiots.jpg",
            show_time="4:00 PM",
            screen="Screen 2"
        ),
        Movie(
            title="Dunki",
            description="An emotional journey of dreams and returning home.",
            genre="Drama",
            image="static//Assests//Dunki.jpg",
            show_time="6:30 PM",
            screen="Screen 3"
        ),
        Movie(
            title="Leo",
            description="Mass action entertainer filled with mystery and rage.",
            genre="Thriller",
            image="static//Assests//Leo.jpg",
            show_time="9:00 PM",
            screen="Screen 1"
        ),
        Movie(
            title="Chhava",
            description="A historical epic based on the life of Chhatrapati Sambhaji Maharaj, showcasing his bravery, intelligence, and sacrifice for the Maratha Empire.",
            genre="Historical Drama",
            image="static//Assests//Chhaava.jpg",
            show_time="7:30 PM",
            screen="Screen 2"
        ),
        Movie(
            title="Raid 2",
            description="A high-octane crime thriller following an honest officer’s battle against corruption and power in the system.",
            genre="Crime Thriller",
            image="static//Assests//Raid-2.jpg",
            show_time="8:30 PM",
            screen="Screen 2"
        ),
        Movie(
            title="Sky Force",
            description="Inspired by true events, this patriotic film showcases the bravery of Indian Air Force officers in a daring mission.",
            genre="Action Drama",
            image="static//Assests//SkyForce.jpg",
            show_time="6:30 PM",
            screen="Screen 3"
        ),
        Movie(
            title="Kantara Chapter 1",
            description="A mythological action drama exploring the origins of divine folklore set in the forests of coastal Karnataka.",
            genre="Mythological Action",
            image="static//Assests//Kantaara.jpg",
            show_time="9:00 PM",
            screen="Screen 4"
        ),
        Movie(
            title="Kill",
            description="A gripping action thriller where a soldier faces brutal odds aboard a train under siege.",
            genre="Action Thriller",
            image="static//Assests//Kill.jpg",
            show_time="10:30 PM",
            screen="Screen 5"
        ),
        Movie(
            title="Sooryavanshi",
            description="An action-packed cop drama following an elite officer tackling terrorism and national threats.",
            genre="Action",
            image="static//Assests//Sooryavanshi.jpg",
            show_time="7:00 PM",
            screen="Screen 1"
        ),
        Movie(
            title="Brahmastra",
            description="A fantasy adventure where a young man discovers his divine connection with the cosmic weapon Brahmastra.",
            genre="Fantasy Adventure",
            image="static//Assests//Brahmsatra.jpg",
            show_time="9:15 PM",
            screen="Screen 2"
        ),
        Movie(
            title="The Kashmir Files",
            description="A powerful drama that sheds light on the untold stories of Kashmiri Pandits and their exodus.",
            genre="Historical Drama",
            image="static//Assests//The kashmir files.jpg",
            show_time="6:45 PM",
            screen="Screen 3"       
        ),
        Movie(
            title="Sam Bahadur",
            description="A biopic on Field Marshal Sam Manekshaw, chronicling his military brilliance and leadership.",
            genre="Biographical Drama",
            image="static//Assests//Sam Bahadur.jpg",
            show_time="8:00 PM",
            screen="Screen 4"
        ),
        Movie(
            title="Ludo",
            description="A quirky dark comedy connecting four lives through fate, chaos, and coincidence.",
            genre="Dark Comedy",
            image="static//Assests//LUDO.jpg",
            show_time="5:45 PM",
            screen="Screen 5"
        ),
        Movie(
            title="Sikandar",
            description="An inspiring journey of a man rising from struggle to power with grit and courage.",
            genre="Action Drama",
            image="static//Assests//Sikandar.jpg",
            show_time="8:45 PM",
            screen="Screen 1"
        ),
        Movie(
            title="12th Fail",
            description="A motivational drama based on real-life stories of UPSC aspirants who overcome failure through determination.",
            genre="Inspirational Drama",
            image="static//Assests//12th Fail.jpg",
            show_time="7:15 PM",
            screen="Screen 2"
        ),
        Movie(
            title="Bulbbul",
            description="A mystical period drama blending folklore and feminism through hauntingly beautiful storytelling.",
            genre="Horror Fantasy",
            image="static//Assests//Bulbbul.jpg",
            show_time="9:45 PM",
            screen="Screen 3"
        ),
        Movie(
            title="Munjya",
            description="A horror comedy rooted in Indian folklore, where a mythical ghost causes hilarious chaos.",
            genre="Horror Comedy",
            image="static//Assests//Munjya.jpg",
            show_time="6:00 PM",
            screen="Screen 4"
        ),
        Movie(
            title="1920",
            description="A spine-chilling horror story of a haunted mansion and a couple facing supernatural forces.",
            genre="Horror",
            image="static//Assests//1920.jpg",
            show_time="10:00 PM",
            screen="Screen 5"
        ),
        Movie(
            title="Chello Divas",
            description="A Gujarati comedy about friendship, college life, and youthful adventures.",
            genre="Comedy Drama",
            image="static//Assests//Chello divas.jpg",
            show_time="5:30 PM",
            screen="Screen 1"
        ),
        Movie(
            title="3 Ekka",
            description="A Gujarati comedy where three friends take a wild route to quick success through a quirky plan.",
            genre="Comedy",
            image="static//Assests//3 ekka.jpg",
            show_time="8:15 PM",
            screen="Screen 2"
        ),
        Movie(
            title="Gujju Bhai",
            description="A hilarious Gujarati entertainer full of family fun, mischief, and relatable humor.",
            genre="Comedy",
            image="static//Assests//Gujjubhai.jpg",
            show_time="6:45 PM",
            screen="Screen 3"
        ),
        Movie(
            title="Chal Jivi Laie",
            description="A heartwarming Gujarati drama exploring a father-son journey that changes their outlook on life.",
            genre="Drama",
            image="static//Assests//chal jivi laye.jpg",
            show_time="7:30 PM",
            screen="Screen 4"
        ),
        Movie(
            title="Ghantadi",
            description="A Gujarati comedy revolving around fun, confusion, and local humor with a social twist.",
            genre="Comedy",
            image="static//Assests//Ghantadi.jpg",
            show_time="9:00 PM",
            screen="Screen 5"
        ),
        Movie(
            title="Pushpa 2",
            description="The continuation of Pushpa Raj’s empire, where power, rebellion, and ambition collide.",
            genre="Action Drama",
            image="static//Assests//pushpa 2.jpg",
            show_time="9:30 PM",
            screen="Screen 1"
        ),
        Movie(
            title="Bahubali: The Epic",
            description="A grand mythological saga of kings, war, betrayal, and destiny that shaped a kingdom.",
            genre="Epic Action",
            image="static//Assests//Bahubali - the epic.jpg",
            show_time="10:15 PM",
            screen="Screen 2"
        ),
        Movie(
            title="Stree 2",
            description="A hilarious horror sequel where the mysterious spirit returns to haunt a small town.",
            genre="Horror Comedy",
            image="static//Assests//stree - 2.jpg",
            show_time="8:00 PM",
            screen="Screen 3"
        ),
        Movie(
            title="Housefull 5",
            description="A madcap comedy filled with confusion, laughter, and over-the-top entertainment.",
            genre="Comedy",
            image="static//Assests//Housefull 5.jpg",
            show_time="6:30 PM",
            screen="Screen 4"
        ),
       Movie(
            title="Bhool Bhulaiyaa 3",
            description="A horror comedy sequel packed with mystery, laughter, and ghostly drama.",
            genre="Horror Comedy",
            image="static//Assests//BB3.jpg",
            show_time="9:45 PM",
            screen="Screen 5"
        ),
       Movie(
            title="Kesari Chapter 2",
            description="A patriotic action drama continuing the tale of valor inspired by the Battle of Saragarhi.",
            genre="War Drama",
            image="static//Assests//Kesari chapter 2.jpg",
            show_time="7:15 PM",
            screen="Screen 1"
        ),
        Movie(
            title="Kabir Singh",
            description="A passionate romantic drama portraying a brilliant yet self-destructive surgeon’s love story.",
            genre="Romantic Drama",
            image="static//Assests//Kabir singh.jpg",
            show_time="8:30 PM",
            screen="Screen 2"
        ),
        Movie(
            title="Animal",
            description="An intense family action drama exploring love, rage, and father-son relationships.",
            genre="Action Drama",
            image="static//Assests//Animal.jpg",
            show_time="9:00 PM",
            screen="Screen 3"
        ),
        Movie(
            title="Andhadhun",
            description="A gripping thriller about a blind pianist entangled in a web of murder and deception.",
            genre="Thriller",
            image="static//Assests//Andhadhun.jpg",
            show_time="7:45 PM",
            screen="Screen 4"
        ),
        Movie(
            title="Uri",
            description="A patriotic war drama based on India’s surgical strike, celebrating valor and strategy.",
            genre="Action War",
            image="static//Assests//URI.jpg",
            show_time="8:00 PM",
            screen="Screen 5"
        ),
    ]

    # ---------- COMMIT TO DATABASE ----------
    db.session.bulk_save_objects(sample_movies)
    db.session.commit()

    print(" All movies added successfully with show timings and screens!")