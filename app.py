import streamlit as st
import datetime
from zoneinfo import ZoneInfo
import math

# List of common timezones
common_timezones = [
    "UTC",
    "America/New_York",
    "America/Chicago",
    "America/Los_Angeles",
    "Europe/London",
    "Europe/Paris",
    "Asia/Kolkata",
    "Asia/Tokyo",
    "Australia/Sydney",
]

# Zodiac signs based on longitude ranges
zodiac_signs = [
    ("Aries", 0, 30),
    ("Taurus", 30, 60),
    ("Gemini", 60, 90),
    ("Cancer", 90, 120),
    ("Leo", 120, 150),
    ("Virgo", 150, 180),
    ("Libra", 180, 210),
    ("Scorpio", 210, 240),
    ("Sagittarius", 240, 270),
    ("Capricorn", 270, 300),
    ("Aquarius", 300, 330),
    ("Pisces", 330, 360),
]

# List of 72 angels with updated details
angels = [
    {"number": 1, "name": "Vehuiah", "zodiac": "Aries", "element": "Fire", "description": "Sparks new beginnings and helps individuals overcome challenges. Supports the undertaking of the Great Work; known for wisdom; patron for liberal arts and sciences. Elevates ranking and status.", "psalm": "3:3", "sigil_desc": None},
    {"number": 2, "name": "Jeliel", "zodiac": "Aries", "element": "Fire", "description": "Promotes love, loyalty, and fidelity in relationships. Invoke to embody artful diplomacy and political acumen; facilitates victory; champion of social justice; sprightly, outgoing, optimistic, energetic, and friendly.", "psalm": "22:19", "sigil_desc": None},
    {"number": 3, "name": "Sitael", "zodiac": "Aries", "element": "Fire", "description": "Protects against adversity and helps manifest goals. A protector. Defends against attacks. Reveals truths. Merciful and compassionate, aids those in need of protection.", "psalm": "91:2", "sigil_desc": None},
    {"number": 4, "name": "Elemiah", "zodiac": "Aries", "element": "Fire", "description": "Encourages career success and helps recover from betrayal. Calms anxiety, stress, depression, and worry. Travel protection, especially by sea or over long distances. Guardian during strenuous voyages. Hard-working, diligent, productive, and conscientious.", "psalm": "6:4", "sigil_desc": None},
    {"number": 5, "name": "Mahasiah", "zodiac": "Aries", "element": "Fire", "description": "Brings peace, harmony, and intellectual enlightenment. Patron of high sciences and occult philosophy. Facilitates learning in theology, alchemy, physics. An educator. Embraces quest for knowledge. Seeks peace, diffuses conflicts.", "psalm": "34:4", "sigil_desc": None},
    {"number": 6, "name": "Lelahel", "zodiac": "Aries", "element": "Fire", "description": "Enhances healing and attracts prosperity. A healing angel. Patron of medical knowledge and science; seeks to cure illness and disease. Guards those on path for greater public recognition and material prosperity.", "psalm": "9:11", "sigil_desc": None},
    {"number": 7, "name": "Achaiah", "zodiac": "Taurus", "element": "Earth", "description": "Assists in patience and understanding life’s mysteries. Guardian and ally to those undertaking greatest challenges; guardian to those on hero’s journey. Can reveal secrets of nature to seekers.", "psalm": "103:8", "sigil_desc": None},
    {"number": 8, "name": "Cahetel", "zodiac": "Taurus", "element": "Earth", "description": "Encourages gratitude and brings blessings to households. Drives away evil spirits, demons, infectious diseases, and rot; protects agriculture, productivity, and harvests. Angel of deep reverence and faith.", "psalm": "95:6", "sigil_desc": None},
    {"number": 9, "name": "Haziel", "zodiac": "Taurus", "element": "Earth", "description": "Offers forgiveness and divine mercy. Facilitates mercy. Favors mentally and emotionally resilient. Extends pardons to penitent wrongdoers. Loves and protects outcasts, vagrants, and vagabonds.", "psalm": "25:6", "sigil_desc": None},
    {"number": 10, "name": "Aladiah", "zodiac": "Taurus", "element": "Earth", "description": "Aids in recovery from illness and personal transformation. Protection from negative influences, purification, and renewal. Helps in healing and spiritual cleansing.", "psalm": "33:22", "sigil_desc": None},
    {"number": 11, "name": "Lauviah", "zodiac": "Taurus", "element": "Earth", "description": "Provides relief from anxiety and deepens spiritual wisdom. Angel of discipline, strong will, and determination. Helps with regulation and temperance. Reveals prophecies through dreams. Lover of music, poetry, fine literature. Ally to innovators.", "psalm": "18:46", "sigil_desc": None},
    {"number": 12, "name": "Hahaiah", "zodiac": "Taurus", "element": "Earth", "description": "Unlocks intuition and helps decipher dreams. Safeguards against adversity. Governs dream world, protects during dream work, lucid dreaming, or astral travel. Guardian of astral realm. Witty, enjoys riddles, protects mortals in astral realm.", "psalm": "10:1", "sigil_desc": None},
    {"number": 13, "name": "Iezalel", "zodiac": "Gemini", "element": "Air", "description": "Strengthens friendships and promotes unity. Sociable and charismatic; teaches adaptability; endows social charisma and magnetism. Endows star quality. Facilitates successful marriages or improves conjugal relations.", "psalm": "98:4", "sigil_desc": None},
    {"number": 14, "name": "Mebahel", "zodiac": "Gemini", "element": "Air", "description": "Brings truth, justice, and fairness. Protects against exploitation. Champion of truth, liberty, and justice. Guardian over prisoners and oppressed. Lover of legal studies, affinity for courts, judges, attorneys.", "psalm": "9:9", "sigil_desc": None},
    {"number": 15, "name": "Hariel", "zodiac": "Gemini", "element": "Air", "description": "Inspires artistic creativity and spiritual purity. Pious angel of moral purity governing arts and sciences; helps discover truths; endows creativity and inspiration; promotes human knowledge of sciences.", "psalm": "128:4", "sigil_desc": None},
    {"number": 16, "name": "Hekamiah", "zodiac": "Gemini", "element": "Air", "description": "Encourages leadership and loyalty. Protector of leaders and pioneers. Guides with strength, courage, ensures victory. Sensitive, loyal nature.", "psalm": "88:1", "sigil_desc": None},
    {"number": 17, "name": "Lauviah", "zodiac": "Gemini", "element": "Air", "description": "Offers protection and serenity during hardships. Wonderful. Angel of discipline, strong will, and determination. Helps with regulation and temperance. Reveals prophecies through dreams. Lover of music, poetry, fine literature. Ally to innovators.", "psalm": "8:9", "sigil_desc": None},
    {"number": 18, "name": "Caliel", "zodiac": "Gemini", "element": "Air", "description": "Defends against injustice and false accusations. Allows discernment of truth in all things. Helps win legal cases. Assists in overcoming adversity.", "psalm": "35:24", "sigil_desc": None},
    {"number": 19, "name": "Leuviah", "zodiac": "Cancer", "element": "Water", "description": "Strengthens memory and aids in emotional healing. Expansive intelligence, excellent memory, and fruitful imagination. Helps bear adversities with patience and acceptance.", "psalm": "40:1", "sigil_desc": None},
    {"number": 20, "name": "Pahaliah", "zodiac": "Cancer", "element": "Water", "description": "Deepens faith and spiritual practices. Redeemer. Helps discover one's vocation, facilitates religious or spiritual calling. Victory over enemies. Dominion over morals.", "psalm": "119:108", "sigil_desc": None},
    {"number": 21, "name": "Nelchael", "zodiac": "Cancer", "element": "Water", "description": "Protects against slander and boosts intellectual pursuits. Thirst for knowledge. Affinity for math and astronomy. Protects against calumny and spells.", "psalm": "31:14", "sigil_desc": None},
    {"number": 22, "name": "Ieiaiel", "zodiac": "Cancer", "element": "Water", "description": "Governs fame, diplomacy, commerce, and travel. It aids in resolving conflicts, protecting against adversity, and fostering clear communication.", "psalm": "121:5", "sigil_desc": "resembling intertwined waves and a crown"},
    {"number": 23, "name": "Melahel", "zodiac": "Cancer", "element": "Water", "description": "Heals physical ailments and supports environmental protection. Healing plants and herbs. Protection in travel. Bold warrior spirit.", "psalm": "121:8", "sigil_desc": None},
    {"number": 24, "name": "Haheuiah", "zodiac": "Cancer", "element": "Water", "description": "Protects travelers and guides those who feel lost. Protection for exiles. Mercy for criminals seeking sincere redemption. Guards against thieves and murderers.", "psalm": "33:18", "sigil_desc": None},
    {"number": 25, "name": "Nith-Haiah", "zodiac": "Leo", "element": "Fire", "description": "Offers access to esoteric knowledge and mystical insight. Dominion over occult sciences and magick. Reveals hidden mysteries to the wise. Peaceful, reserved nature.", "psalm": "9:1", "sigil_desc": None},
    {"number": 26, "name": "Haaiah", "zodiac": "Leo", "element": "Fire", "description": "Encourages diplomacy and helps achieve success in negotiations. Angel of political science and ambition. Wins favors from influential people. Loves truth and peace.", "psalm": "119:145", "sigil_desc": None},
    {"number": 27, "name": "Ierathel", "zodiac": "Leo", "element": "Fire", "description": "Inspires confidence and positivity in difficult times. Protector against slander and unjust attacks. Confounds enemies. Propagates enlightenment.", "psalm": "140:1", "sigil_desc": None},
    {"number": 28, "name": "Seheiah", "zodiac": "Leo", "element": "Fire", "description": "Provides healing and protection from accidents. Protection against catastrophes, accidents, and illness. Prudence and foresight. Long life.", "psalm": "71:12", "sigil_desc": None},
    {"number": 29, "name": "Reyel", "zodiac": "Leo", "element": "Fire", "description": "Strengthens connection to the divine and moral integrity. Liberation from enemies. Protects against false prophets and religious fanaticism. Love of truth.", "psalm": "54:4", "sigil_desc": None},
    {"number": 30, "name": "Omael", "zodiac": "Leo", "element": "Fire", "description": "Brings joy, optimism, and fertility. Multiplies joy and fertility. Patience in despair. Patron of chemists and physicians.", "psalm": "71:5", "sigil_desc": None},
    {"number": 31, "name": "Lecabel", "zodiac": "Virgo", "element": "Earth", "description": "Enhances problem-solving skills and agricultural success. Talent in geometry and astronomy. Solves difficult problems. Loves lucidity.", "psalm": "71:16", "sigil_desc": None},
    {"number": 32, "name": "Vasariah", "zodiac": "Virgo", "element": "Earth", "description": "Supports forgiveness and intellectual development. Clemency and mercy. Good memory, eloquent speech. Helps in legal matters.", "psalm": "33:4", "sigil_desc": None},
    {"number": 33, "name": "Yehuiah", "zodiac": "Virgo", "element": "Earth", "description": "Encourages loyalty and exposes hidden enemies. Subordination to superiors. Reveals traitors. Protects princes.", "psalm": "131:3", "sigil_desc": None},
    {"number": 34, "name": "Lehahiah", "zodiac": "Virgo", "element": "Earth", "description": "Inspires obedience and promotes peaceful coexistence. Obedient nature. Calms anger. Faithful servant.", "psalm": "131:3", "sigil_desc": None},
    {"number": 35, "name": "Chavakiah", "zodiac": "Virgo", "element": "Earth", "description": "Reconciles conflicts and strengthens familial bonds. Reconciliation. Maintains peace in families. Dominion over estates and inheritance.", "psalm": "116:1", "sigil_desc": None},
    {"number": 36, "name": "Menadel", "zodiac": "Virgo", "element": "Earth", "description": "Aids in finding lost objects and regaining employment. Liberation from bad habits. Protects against calumny. Maintains employment.", "psalm": "26:8", "sigil_desc": None},
    {"number": 37, "name": "Aniel", "zodiac": "Libra", "element": "Air", "description": "Promotes spiritual ascension and courage. Victory over obstacles. Breaks vicious cycles. Inspires through sciences.", "psalm": "80:15", "sigil_desc": None},
    {"number": 38, "name": "Haamiah", "zodiac": "Libra", "element": "Air", "description": "Protects against negativity and enhances ritual practices. Prepares for rituals. Protects against lightning and violence. Exorcism.", "psalm": "91:9", "sigil_desc": None},
    {"number": 39, "name": "Rehael", "zodiac": "Libra", "element": "Air", "description": "Encourages compassion and emotional healing. Filial submission. Cures mental illnesses. Paternal love.", "psalm": "30:10", "sigil_desc": None},
    {"number": 40, "name": "Ieiazel", "zodiac": "Libra", "element": "Air", "description": "Offers comfort during grief and aids in creative pursuits. Liberation from oppression. Consoles prisoners. Influences printing and books.", "psalm": "88:14", "sigil_desc": None},
    {"number": 41, "name": "Hahahel", "zodiac": "Libra", "element": "Air", "description": "Inspires faith and moral virtue. Vocation for priesthood. Victory over enemies. Great generosity.", "psalm": "120:2", "sigil_desc": None},
    {"number": 42, "name": "Mikael", "zodiac": "Libra", "element": "Air", "description": "Guides political leaders and promotes harmony. Political authority. Surveillance of empires. Influences voyages.", "psalm": "121:7", "sigil_desc": None},
    {"number": 43, "name": "Veuliah", "zodiac": "Scorpio", "element": "Water", "description": "Brings prosperity and victory in endeavors. Prosperity. Confounds the wicked. Dominion over great captains.", "psalm": "88:13", "sigil_desc": None},
    {"number": 44, "name": "Yelahiah", "zodiac": "Scorpio", "element": "Water", "description": "Provides protection during travel and legal battles. Success in arms. Loyalty of soldiers. Protects against sedition.", "psalm": "119:108", "sigil_desc": None},
    {"number": 45, "name": "Sealiah", "zodiac": "Scorpio", "element": "Water", "description": "Motivates and energizes individuals. Confounds the wicked. Raises up the oppressed. Dominion over vegetation.", "psalm": "94:18", "sigil_desc": None},
    {"number": 46, "name": "Ariel", "zodiac": "Scorpio", "element": "Water", "description": "Reveals hidden truths, treasures, and insights through dreams or intuition. It supports perception, discovery, and spiritual revelations.", "psalm": "145:9", "sigil_desc": "a key unlocking a door amid swirling mists"},
    {"number": 47, "name": "Asaliah", "zodiac": "Scorpio", "element": "Water", "description": "Enhances contemplation and spiritual insight. Contemplation of divine. Elevates the soul. Discovers hidden secrets.", "psalm": "105:1", "sigil_desc": None},
    {"number": 48, "name": "Mihael", "zodiac": "Scorpio", "element": "Water", "description": "Promotes harmony in relationships and fertility. Unity between spouses. Peace and marital harmony. Fidelity.", "psalm": "98:2", "sigil_desc": None},
    {"number": 49, "name": "Vehuel", "zodiac": "Sagittarius", "element": "Fire", "description": "Elevates the soul and encourages generosity. Sublime and exalted. Generosity. Sensitivity to higher realms.", "psalm": "145:3", "sigil_desc": None},
    {"number": 50, "name": "Daniel", "zodiac": "Sagittarius", "element": "Fire", "description": "Offers mercy and aids in decision-making. Eloquence. Influences judges. Inspires decisions favoring innocents.", "psalm": "145:8", "sigil_desc": None},
    {"number": 51, "name": "Hahasiah", "zodiac": "Sagittarius", "element": "Fire", "description": "Provides healing and alchemical knowledge. Universal medicine. Cures melancholy. Reveals secrets of nature.", "psalm": "104:31", "sigil_desc": None},
    {"number": 52, "name": "Imamiah", "zodiac": "Sagittarius", "element": "Fire", "description": "Protects against errors and promotes humility. Destroys enemies. Exalts the humiliated. Vigorous work ethic.", "psalm": "7:17", "sigil_desc": None},
    {"number": 53, "name": "Nanael", "zodiac": "Sagittarius", "element": "Fire", "description": "Supports spiritual communication and meditation. Spiritual communication. Inspires meditation on divine. Teachers and men of law.", "psalm": "119:75", "sigil_desc": None},
    {"number": 54, "name": "Nithael", "zodiac": "Sagittarius", "element": "Fire", "description": "Brings stability and longevity. Eternal youth. Legitimacy and stability to empires. Mercy to subjects.", "psalm": "103:19", "sigil_desc": None},
    {"number": 55, "name": "Mebahiah", "zodiac": "Capricorn", "element": "Earth", "description": "Enhances intellectual clarity and moral integrity. Lucidity and consolation. Inspires religious sentiment. Virtuous living.", "psalm": "102:12", "sigil_desc": None},
    {"number": 56, "name": "Poyel", "zodiac": "Capricorn", "element": "Earth", "description": "Associated with modesty, moderation, a good sense of humor, and success achieved through talent and good conduct. Linked to fortune, fame, and the fulfillment of wishes. Influences individuals to be humble, optimistic, and guided towards divine success. Seen as the quiet force behind achieving goals, realizing dreams, and receiving answered prayers.", "psalm": "145:14", "sigil_desc": None},
    {"number": 57, "name": "Nemamiah", "zodiac": "Capricorn", "element": "Earth", "description": "Aids in prosperity and military success. Prosperity. Liberation of prisoners. Brave in battle. Loves military careers.", "psalm": "115:11", "sigil_desc": None},
    {"number": 58, "name": "Yeialel", "zodiac": "Capricorn", "element": "Earth", "description": "Heals mental ailments and promotes clarity. Combats sorrow. Patron of ironwork and blacksmiths. Mental agility.", "psalm": "6:3", "sigil_desc": None},
    {"number": 59, "name": "Harahel", "zodiac": "Capricorn", "element": "Earth", "description": "Protects children and aids in financial matters. Intellectual curiosity. Fertility. Protects treasuries and archives.", "psalm": "113:9", "sigil_desc": None},
    {"number": 60, "name": "Mitzrael", "zodiac": "Capricorn", "element": "Earth", "description": "Heals illnesses and promotes loyalty. Reparation and virtue. Liberation from persecutors. Inspires loyalty.", "psalm": "145:17", "sigil_desc": None},
    {"number": 61, "name": "Umabel", "zodiac": "Aquarius", "element": "Air", "description": "Strengthens friendships and affinity. Affinity for astronomy and physics. Obtains friendships. Pleasurable travel.", "psalm": "113:2", "sigil_desc": None},
    {"number": 62, "name": "Iahhel", "zodiac": "Aquarius", "element": "Air", "description": "Offers wisdom and enlightenment. Supreme knowledge. Modest living. Marital tranquility. Philosopher's stone.", "psalm": "119:159", "sigil_desc": None},
    {"number": 63, "name": "Anauel", "zodiac": "Aquarius", "element": "Air", "description": "Protects commerce and promotes unity. Unity of all things. Protects against accidents. Inspires bankers and merchants.", "psalm": "37:4", "sigil_desc": None},
    {"number": 64, "name": "Mehiel", "zodiac": "Aquarius", "element": "Air", "description": "Inspires writers and protects against negativity. Vivification. Protects against rabies and ferocious animals. Inspires writers.", "psalm": "33:18", "sigil_desc": None},
    {"number": 65, "name": "Damabiah", "zodiac": "Aquarius", "element": "Air", "description": "Offers wisdom and protection at sea. Fountain of wisdom. Success in naval enterprises. Protects against sorcery.", "psalm": "90:13", "sigil_desc": None},
    {"number": 66, "name": "Manakel", "zodiac": "Aquarius", "element": "Air", "description": "Heals sleep disorders and promotes peace. Goodness. Calms anger. Dominion over vegetation. Cures sleep disorders.", "psalm": "38:21", "sigil_desc": None},
    {"number": 67, "name": "Eyael", "zodiac": "Pisces", "element": "Water", "description": "Transforms sorrow into joy and aids in studies. Consolation in adversity. Love of solitude. Wisdom in philosophy.", "psalm": "37:4", "sigil_desc": None},
    {"number": 68, "name": "Habuhiah", "zodiac": "Pisces", "element": "Water", "description": "Heals diseases and supports agriculture. Healing. Fertility of earth. Successful harvests.", "psalm": "106:1", "sigil_desc": None},
    {"number": 69, "name": "Rochel", "zodiac": "Pisces", "element": "Water", "description": "Helps find lost objects and promotes justice. Restitution. Finds lost objects. Influences renown through talent.", "psalm": "16:5", "sigil_desc": None},
    {"number": 70, "name": "Yabamiah", "zodiac": "Pisces", "element": "Water", "description": "Facilitates creation, regeneration, and alchemical transformation. It inspires philosophical understanding, harmony with nature, and the ability to manifest ideas into reality.", "psalm": "Genesis 1:1", "sigil_desc": "a phoenix rising from water"},
    {"number": 71, "name": "Haiaiel", "zodiac": "Pisces", "element": "Water", "description": "Provides courage and protection against evil. Discernment. Victory over traitors. Protects against conspiracies.", "psalm": "109:30", "sigil_desc": None},
    {"number": 72, "name": "Mumiah", "zodiac": "Pisces", "element": "Water", "description": "Brings completion and success in endeavors. Brings undertakings to successful conclusion. Longevity and success in medicine.", "psalm": "116:7", "sigil_desc": None}
]

# Special days and elements
special_days = [(5, 31), (8, 12), (10, 24), (1, 5), (3, 19)]
elements = ["Fire", "Water", "Air", "Earth", "Ether"]

# Element qualities
element_qualities = {
    "Fire": "passion, energy, initiative",
    "Water": "emotional depth, intuition, nurturing",
    "Air": "intellect, communication, adaptability",
    "Earth": "stability, practicality, sensuality"
}

# Element invocation details
element_invocations = {
    "Fire": {
        "colors": "red or orange",
        "imagery": "flames or sunlight",
        "phases": "sunrise or full sun",
        "openness": "energetic openness"
    },
    "Water": {
        "colors": "blue or sea-green",
        "imagery": "oceans or rivers",
        "phases": "moon phases (especially full moons)",
        "openness": "emotional openness"
    },
    "Air": {
        "colors": "yellow or light blue",
        "imagery": "wind or clouds",
        "phases": "windy days or clear skies",
        "openness": "mental openness"
    },
    "Earth": {
        "colors": "green or brown",
        "imagery": "mountains or soil",
        "phases": "stable weather or new moons",
        "openness": "grounded openness"
    }
}

element_emojis = {
    "Fire": "🔥",
    "Water": "💧",
    "Air": "💨",
    "Earth": "🌍"
}

def get_angel(num):
    return next((a for a in angels if a["number"] == num), None)

def get_zodiac_sign(lon):
    lon = lon % 360
    for sign, start, end in zodiac_signs:
        if start <= lon < end:
            return sign
    return "Pisces"

def julian_day(dt):
    year = dt.year
    month = dt.month
    day = dt.day
    hour = dt.hour + dt.minute / 60 + dt.second / 3600
    if month < 3:
        year -= 1
        month += 12
    a = math.floor(year / 100)
    b = 2 - a + math.floor(a / 4)
    jd = math.floor(365.25 * (year + 4716)) + math.floor(30.6001 * (month + 1)) + day + b - 1524.5
    return jd + hour / 24

def sun_ecliptic_longitude(dt):
    jd = julian_day(dt)
    D = jd - 2451545.0
    g_deg = (357.529 + 0.98560028 * D) % 360
    q_deg = (280.459 + 0.98564736 * D) % 360
    g_rad = math.radians(g_deg)
    L_deg = (q_deg + 1.915 * math.sin(g_rad) + 0.020 * math.sin(2 * g_rad)) % 360
    if L_deg < 0:
        L_deg += 360
    return L_deg

st.title("Angels Calculator - Precise Edition ✨")

mode = st.radio("Select Mode 🔮", ("Current Moment 🌟", "Birth Date 👶"))

default_tz = "Asia/Kolkata"
timezone = st.selectbox(
    "Select time zone 🌍",
    options=common_timezones,
    index=common_timezones.index(default_tz)
)

if mode == "Current Moment 🌟":
    if st.button("Refresh 🔄"):
        st.rerun()
    tz = ZoneInfo(timezone)
    dt = datetime.datetime.now(tz)
    date_str = dt.strftime('%B %d, %Y')
    time_str = dt.strftime('%H:%M')
    moment_desc = f"the current moment of {date_str}, at {time_str} in {timezone}"
    makeup_desc = "current energetic makeup ⚡"
    affinity_desc = "the present moment—qualities that resonate with the now 🌈"
    ritual_date = "the current date 📅"
    special_date_desc = "The current date 📆"
else:
    birth_date = st.date_input(
        "Select birth date 🎂",
        min_value=datetime.date(1900, 1, 1),
        max_value=datetime.date(2100, 12, 31),
        value=datetime.date.today()
    )
    birth_time = st.time_input(
        "Select birth time ⏰",
        value=datetime.time(12, 0)
    )
    dt = datetime.datetime.combine(birth_date, birth_time)
    tz = ZoneInfo(timezone)
    dt = dt.replace(tzinfo=tz)
    date_str = birth_date.strftime('%B %d, %Y')
    time_str = birth_time.strftime('%H:%M')
    moment_desc = f"your birth details of {date_str}, at {time_str} in {timezone}—marking the moment of your birth 👼"
    makeup_desc = "personal energetic makeup ✨"
    affinity_desc = "life's queries—qualities that resonate with your unique design 🌟"
    ritual_date = "your birth date 🎉"
    special_date_desc = "Your birth date 🎂"

month = dt.month
day = dt.day

current_utc = dt.astimezone(datetime.timezone.utc)

longitude = sun_ecliptic_longitude(current_utc)
physical_num = int(longitude // 5) + 1
emotional_num = ((physical_num - 1 + 24) % 72) + 1
intellectual_num = ((physical_num - 1 + 48) % 72) + 1

physical_angel = get_angel(physical_num)
emotional_angel = get_angel(emotional_num)
intellectual_angel = get_angel(intellectual_num)

zodiac_sign = get_zodiac_sign(longitude)

special_message = ""
if (month, day) in special_days:
    special_index = special_days.index((month, day))
    special_message = f"\n\n{special_date_desc} {dt.strftime('%B %d')} is one of the special days linked to the five elements. You are associated with the element: {elements[special_index]} 🌟. People born on these days are said to embody genius qualities and can connect with any angel or elemental forces. ✨"

elements_list = [physical_angel["element"], emotional_angel["element"], intellectual_angel["element"]]
common_element = max(set(elements_list), key=elements_list.count)
element_themes = {
    "Fire": "dynamic, creative, and transformative energies 🔥",
    "Water": "fluidity, empathy, subconscious wisdom, and emotional healing 💧",
    "Air": "intellect, communication, and social harmony 💨",
    "Earth": "stability, practicality, and material manifestation 🌍",
}

sigil_text = ""
for angel in [physical_angel, emotional_angel, intellectual_angel]:
    if angel["sigil_desc"]:
        sigil_text += f"{angel['name']}'s ({angel['sigil_desc']}), "

sigil_text = sigil_text.rstrip(", ") or "traditional Kabbalistic sigils derived from the Rose Cross or Hebrew letters ✍️"

psalm_text = ""
if physical_angel["psalm"]:
    psalm_text = f" (e.g., Psalm {physical_angel['psalm']} for {physical_angel['name']}, focusing on deliverance 📖)"

inv = element_invocations[common_element]
colors = inv["colors"]
imagery = inv["imagery"]
phases = inv["phases"]
openness = inv["openness"]

phys_qual = element_qualities[physical_angel["element"]] + " " + element_emojis[physical_angel["element"]]
emot_qual = element_qualities[emotional_angel["element"]] + " " + element_emojis[emotional_angel["element"]]
intell_qual = element_qualities[intellectual_angel["element"]] + " " + element_emojis[intellectual_angel["element"]]

# Generate descriptive text
text = f"""
For this personal application, based on {moment_desc}. This falls under the zodiac sign of {zodiac_sign} ♋.{special_message}

To calculate the birth angels, we start with the physical (or incarnation/guardian) angel 👼, which corresponds to the exact position of the Sun ☀️ at birth within the standard Kabbalistic assignment of the 72 angels to the zodiac (each governing a 5-degree segment). Based on the precise time ⏳, it aligns with angel number {physical_angel['number']}: {physical_angel['name']} (also spelled variations like Yeiaiel or Yeiayel for some).

From there, the emotional (or heart) angel ❤️ is determined by adding 24 to the physical angel’s number (representing a 120-degree trine aspect in the zodiac for harmonious emotional support). The intellectual (or intellect) angel 🧠 adds 48 (a 240-degree trine for mental alignment). If the result exceeds 72, subtract 72 to cycle back. This yields:

•  Physical Angel 👼: {physical_angel['name']} (No. {physical_angel['number']}) – {physical_angel['description']}. Zodiac: {physical_angel['zodiac']} ({physical_angel['element']} element – {phys_qual}).

•  Emotional Angel ❤️: {emotional_angel['name']} (No. {emotional_angel['number']}) – {emotional_angel['description']}. Zodiac: {emotional_angel['zodiac']} ({emotional_angel['element']} element – {emot_qual}).

•  Intellectual Angel 🧠: {intellectual_angel['name']} (No. {intellectual_angel['number']}) – {intellectual_angel['description']}. Zodiac: {intellectual_angel['zodiac']} ({intellectual_angel['element']} element – {intell_qual}).

All three angels share the {common_element} element {element_emojis[common_element]}, emphasizing themes of {element_themes[common_element]} in your {makeup_desc}. This alignment suggests a natural affinity for intuitive reasoning, adaptive problem-solving, and connecting deeply with {affinity_desc}.

For invocation, align practices with {common_element}’s energies {element_emojis[common_element]}: use {colors} colors 🎨, {imagery} imagery (e.g., {imagery}), {phases}, and {openness}. Here’s how to engage each:

•  Meditation 🧘: Sit quietly near {imagery} or with a representation of it. Visualize a soft {colors} light enveloping you. For {physical_angel['name']}, focus on diplomatic resolutions in your life; for {emotional_angel['name']}, seek revelations on hidden questions; for {intellectual_angel['name']}, contemplate personal transformation. Chant or affirm the angel’s name (e.g., “{physical_angel['name']}, guide my words with clarity”) for 5–10 minutes daily.

•  Sigils ✒️: Each angel has a traditional sigil derived from the Kabbalistic Rose Cross or Hebrew letters. Draw {sigil_text} on paper. Meditate on it while burning frankincense (for {common_element}’s mystical vibe) or placing it under moonlight 🌕.

•  Rituals 🕯️: Create a simple altar with {imagery}, a chalice or symbol of {common_element}, and {physical_angel['zodiac']}/{emotional_angel['zodiac']}/{intellectual_angel['zodiac']} symbols. On {ritual_date} (or any {common_element}-ruled day like Monday), light a {colors} candle and recite a psalm associated with the angel{psalm_text}. Offer thanks for guidance, then journal insights 📓. Repeat seasonally to strengthen the connection, always with pure intent for balance and growth 🌱.

This framework can be adapted for any moment—simply compute the Sun's position for the physical angel, then apply the +24/+48 formula for the others.
"""

st.markdown(text)
