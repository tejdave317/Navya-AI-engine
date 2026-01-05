# Navya-AI-Engine
An implementation of Navya Nyaya Logic for Expainable AI
# logic_engine.py

class AvacchedakaEngine:
    """
    यह क्लास नव्य-न्याय के अवच्छेदक-अवच्छिन्न सिद्धांत को लागू करती है।
    यह AI प्रतिक्रियाओं में अस्पष्टता को रोकने के लिए 'संदर्भ सीमांकक' (Context Delimiter) के रूप में कार्य करता है।
    """
    def _init_(self):
        # ज्ञान आधार (Knowledge Base): सीमाओं (Avacchedakas) को परिभाषित करना
        # संरचना: {शब्द: {संदर्भ_सीमांकक: सीमित_अर्थ}}
        self.knowledge_base = {
            "Tiger": {
                "Wildlife": "Panthera Tigris (पशु) - भारत में संख्या: ~3000। संरक्षित प्रजाति।",
                "Sports": "उपनाम/रूपक - उदाहरण: विराट कोहली या 'टाइगर' पटौदी।",
                "Stock Market": "एक तेजी से निवेश करने वाला या आक्रामक शेयर।",
                "Legal": "वन्यजीव संरक्षण अधिनियम, 1972 के तहत संरक्षित इकाई।"
            },
            "Bank": {
                "River": "जल निकाय के किनारे की भूमि (तट)।",
                "Finance": "धन प्राप्त करने, उधार देने और सुरक्षित रखने वाली संस्था।",
                "Aviation": "विमान को पार्श्व रूप से झुकाना।"
            },
            "Court": {
                "Legal": "न्यायाधीश की अध्यक्षता वाला न्यायाधिकरण (अदालत)।",
                "Sports": "टेनिस जैसे खेल खेलने के लिए एक चतुर्भुज क्षेत्र।"
            }
        }

    def resolve_meaning(self, word, context_delimiter):
        """
        इनपुट: एक शब्द और उसका संदर्भ (अवच्छेदक)।
        आउटपुट: विशिष्ट, सीमित अर्थ (अवच्छिन्न)।
        """
        # इनपुट को सामान्य करें (Capitalization त्रुटियों को संभालने के लिए)
        word = word.title()
        context_delimiter = context_delimiter.title()
        
        # जांचें कि क्या शब्द हमारे ज्ञान आधार में मौजूद है
        if word in self.knowledge_base:
            # जांचें कि क्या उस शब्द के लिए संदर्भ मौजूद है
            if context_delimiter in self.knowledge_base[word]:
                return self.knowledge_base[word][context_delimiter]
            else:
                available = list(self.knowledge_base[word].keys())
                return f"त्रुटि: '{word}' के लिए संदर्भ '{context_delimiter}' परिभाषित नहीं है। उपलब्ध संदर्भ: {available}"
        else:
            return f"त्रुटि: शब्द '{word}' अवच्छेदक डेटाबेस में नहीं मिला।"

            
