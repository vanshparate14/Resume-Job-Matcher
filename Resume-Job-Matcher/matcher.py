import math
import string
import os
import sys
try:
    import fitz  # PyMuPDF
    import mammoth
except ImportError:
    print("❌ Install deps: pip install PyMuPDF mammoth")
    sys.exit(1)

# ----------------------------------
# Step 1: Extract Text from Any File
# ----------------------------------
def extract_text(path):
    ext = os.path.splitext(path)[1].lower()
    try:
        if ext == '.txt':
            with open(path, "r", encoding="utf-8") as f:
                return f.read().lower()
        elif ext == '.pdf':
            doc = fitz.open(path)
            text = ""
            for page in doc:
                text += page.get_text().lower()
            doc.close()
            return text
        elif ext == '.docx':
            with open(path, "rb") as f:
                result = mammoth.extract_raw_text(f)
            return result.value.lower()
        else:
            raise ValueError(f"Unsupported file type: {ext}. Use TXT, PDF, DOCX.")
    except Exception as e:
        raise ValueError(f"Error reading {path}: {str(e)}")


# ----------------------------------
# Step 2: Text Preprocessing (unchanged)
# ----------------------------------
def preprocess(text):
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    stopwords = {
        "and", "or", "the", "is", "in", "at", "of",
        "a", "an", "with", "for", "to"
    }
    return [w for w in words if w not in stopwords]


# ----------------------------------
# Step 3: Vocabulary Creation (unchanged)
# ----------------------------------
def create_vocabulary(doc1, doc2):
    return list(set(doc1 + doc2))


# ----------------------------------
# Step 4: Term Frequency (unchanged)
# ----------------------------------
def term_frequency(words, vocabulary):
    return [words.count(term) for term in vocabulary]


# ----------------------------------
# Step 5: Cosine Similarity (unchanged)
# ----------------------------------
def cosine_similarity(vec1, vec2):
    dot_product = sum(a*b for a, b in zip(vec1, vec2))
    magnitude1 = math.sqrt(sum(a*a for a in vec1))
    magnitude2 = math.sqrt(sum(b*b for b in vec2))
    if magnitude1 == 0 or magnitude2 == 0:
        return 0
    return dot_product / (magnitude1 * magnitude2)


# ----------------------------------
# Step 6: Analyze Mismatch & Reasons
# ----------------------------------
def analyze_mismatch(resume_words, job_words, vocabulary, resume_vec, job_vec):
    reasons = []
    strengths = []
    threshold = 1  # TF diff threshold for 'missing'
    
    for i, term in enumerate(vocabulary):
        job_tf = job_vec[i]
        resume_tf = resume_vec[i]
        if job_tf > resume_tf + threshold:
            reasons.append(f"Missing '{term}' (job: {job_tf}x, resume: {resume_tf}x)")
        elif resume_tf > job_tf + threshold:
            strengths.append(f"Strong '{term}' (resume: {resume_tf}x vs job: {job_tf}x)")
    
    recs = reasons[:5] if reasons else ["Great overall match! No major gaps."]
    if strengths:
        recs.append("Strengths: " + ", ".join(strengths[:3]))
    
    return {
        'reasons': reasons,
        'recommendations': recs,
        'total_gaps': len(reasons)
    }


# ----------------------------------
# Main Match Analysis
# ----------------------------------
def calculate_match(resume_path, job_path):
    resume_text = extract_text(resume_path)
    job_text = extract_text(job_path)
    
    resume_words = preprocess(resume_text)
    job_words = preprocess(job_text)
    
    vocabulary = create_vocabulary(resume_words, job_words)
    resume_vector = term_frequency(resume_words, vocabulary)
    job_vector = term_frequency(job_words, vocabulary)
    
    similarity = cosine_similarity(resume_vector, job_vector)
    match_score = round(similarity * 100, 2)
    
    analysis = analyze_mismatch(resume_words, job_words, vocabulary, resume_vector, job_vector)
    
    return {
        'score': match_score,
        'analysis': analysis
    }


# ----------------------------------
# Enhanced CLI Output
# ----------------------------------
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python matcher.py <resume_file> <job_file>")
        print("Supports: TXT, PDF, DOCX")
        sys.exit(1)
    
    resume_path, job_path = sys.argv[1], sys.argv[2]
    
    try:
        result = calculate_match(resume_path, job_path)
        print(f"\n✅ Resume–Job Match Score: {result['score']}%")
        
        if result['score'] >= 80:
            print("🎉 Excellent fit!")
        elif result['score'] >= 60:
            print("👍 Good fit, minor improvements possible.")
        else:
            print("⚠️ Needs improvement.")
        
        print("\n📋 Why it may not match (top gaps):")
        for rec in result['analysis']['recommendations']:
            print(f"  • {rec}")
            
        if not result['analysis']['reasons']:
            print("  ✅ No significant gaps found!")
            
    except Exception as e:
        print(f"❌ Error: {str(e)}")

