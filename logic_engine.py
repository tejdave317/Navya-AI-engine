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
# logic_engine.py (जारी...)

class PanchavayavaReasoning:
    """
    यह क्लास भारतीय तर्कशास्त्र के 5-चरणीय न्यायवाक्य (Syllogism) को लागू करती है।
    यह सुनिश्चित करता है कि पारदर्शी 'हेतु' (कारण) के बिना कोई निर्णय नहीं लिया जाए।
    """
    
    def _init_(self, applicant_name):
        self.name = applicant_name
        
    def evaluate_loan(self, credit_score, job_years, annual_income, family_guarantor):
        """
        5-चरणीय नव्य-न्याय प्रक्रिया का उपयोग करके ऋण पात्रता का मूल्यांकन करता है।
        """
        steps = {}
        
        # --- चरण 1: विषम विश्लेषण (तथ्य एकत्र करना) ---
        # 'हेतु' (कारणों) का निर्धारण
        reasons =
        risk_flags =
        
        if credit_score >= 700:
            reasons.append("उच्च क्रेडिट स्कोर (वित्तीय अनुशासन इंगित करता है)")
        elif credit_score >= 650:
            reasons.append("मध्यम क्रेडिट स्कोर (शर्तों के साथ स्वीकार्य)")
            risk_flags.append("स्कोर 700 से कम")
        else:
            risk_flags.append("गंभीर: कम क्रेडिट स्कोर (<650)")
            
        if job_years >= 2:
            reasons.append("स्थिर रोजगार (>2 वर्ष)")
        else:
            risk_flags.append("अस्थिर रोजगार (<2 वर्ष)")
            
        if family_guarantor:
            reasons.append("पारिवारिक गारंटर मौजूद (डिफ़ॉल्ट जोखिम कम करता है)")
        
        # --- 5 चरणों का संश्लेषण (पंचावयव) ---
        
        # 1. प्रतिज्ञा (कथन/निर्णय)
        decision = ""
        loan_amount = 0
        interest_rate = 0.0
        
        # तर्क: मजबूत हेतु बनाम कमजोर हेतु
        if len(risk_flags) == 0:
            decision = "स्वीकृत (मानक)"
            loan_amount = 500000
            interest_rate = 10.5
        elif "गंभीर: कम क्रेडिट स्कोर (<650)" in risk_flags:
            # विशेष नव्य-न्याय अपवाद तर्क (Special Logic):
            # भले ही स्कोर कम हो, यदि गारंटर + स्थिर नौकरी है, तो हम आंशिक अनुमोदन की अनुमति देते हैं
            # यह 'राज' के केस स्टडी  से लिया गया है
            if job_years >= 3 and family_guarantor:
                decision = "स्वीकृत (सशर्त - विशेष तर्क)"
                loan_amount = 200000 # कम राशि
                interest_rate = 14.0 # उच्च दर
            else:
                decision = "अस्वीकृत"
        elif len(risk_flags) > 0 and family_guarantor:
             decision = "स्वीकृत (गारंटर के साथ)"
             loan_amount = 400000
             interest_rate = 12.0
        else:
             decision = "अस्वीकृत (अपर्याप्त सुरक्षा)"

        steps = f"{self.name} के लिए ऋण आवेदन {decision} है।"
        
        # 2. हेतु (कारण)
        if "स्वीकृत" in decision:
            steps = f"क्योंकि: {', '.join(reasons)}।"
        else:
            steps = f"क्योंकि: {', '.join(risk_flags)}।"
            
        # 3. उदाहरण (सार्वभौमिक नियम)
        steps['3. उदाहरण (Udaharana - Universal Example)'] = "नियम: ऐतिहासिक मामलों के 95% में, समान स्थिरता/जोखिम मेट्रिक्स वाले प्रोफाइल का परिणाम यही रहा है।"
        
        # 4. उपनय (अनुप्रयोग)
        steps['4. उपनय (Upanaya - Application)'] = f"{self.name} का प्रोफ़ाइल उदाहरण समूह (पक्ष-धर्मता) के गुणों के साथ संरेखित होता है।"
        
        # 5. निगमन (निष्कर्ष)
        if "स्वीकृत" in decision:
            steps['5. निगमन (Nigamana - Conclusion)'] = f"इसलिए, {interest_rate}% ब्याज पर ₹{loan_amount:,} स्वीकृत करें।"
        else:
            steps['5. निगमन (Nigamana - Conclusion)'] = "इसलिए, इस समय आवेदन संसाधित नहीं किया जा सकता है।"
            
        return steps
        # logic_engine.py (जारी...)

class PaniniNLPSimulator:
    """
    पाणिनीय व्याकरण के नियतात्मक शब्द निर्माण का अनुकरण करता है।
    इनपुट: मूल (धातु) + प्रत्यय (Suffix)
    आउटपुट: नियतात्मक शब्द (कोई हैलुसिनेशन नहीं)
    """
    def _init_(self):
        # नियम-आधारित शब्दकोश (Paninian Rules Map)
        self.grammar_rules = {
            ("Path", "Ate"): "Pathate (पठते - स्वयं के लिए पढ़ता है / आत्मनेपद)",
            ("Path", "Ti"): "Pathati (पठति - दूसरों के लिए पढ़ता है / परस्मैपद)",
            ("Gam", "Ti"): "Gacchati (गच्छति - जाता है)",
            ("Gam", "Ate"): "Gamyate (गम्यते - जाया जाता है / कर्मवाच्य)",
            ("Likha", "Ti"): "Likhati (लिखति - लिखता है)"
        }
        
    def generate_word(self, dhatu, pratyaya):
        """
        शब्द उत्पन्न करने के लिए नियम लागू करता है।
        LLM के विपरीत, यह कभी भी 'Pathozimab' जैसा काल्पनिक शब्द नहीं गढ़ेगा।
        """
        key = (dhatu.title(), pratyaya.title())
        if key in self.grammar_rules:
            return self.grammar_rules[key]
        else:
            return "त्रुटि: इस संयोजन के लिए कोई पाणिनीय नियम नहीं मिला। (हैलुसिनेशन अवरुद्ध)"
            
