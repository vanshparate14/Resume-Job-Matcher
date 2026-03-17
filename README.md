# Resume-Job Matcher 🚀

[![Match Score](https://img.shields.io/badge/Match%20Score-85%25-brightgreen)](https://example.com)

**Intelligent Resume-Job Matching System** - Uses NLP & Cosine Similarity to score how well your resume matches a job description. CLI + Web UI. Supports TXT, PDF, DOCX.

## ✨ Features
- **Multi-format**: TXT, PDF, DOCX files
- **Smart Scoring**: Cosine similarity with term frequency vectors
- **Gap Analysis**: Top missing keywords + recommendations
- **Dual Interface**:
  - CLI: `python matcher.py resume.pdf job.txt`
  - Web: Open `index.html` in browser
- **Fast**: Instant results, no training needed

## 📋 Quick Start

### CLI (Python)
```bash
# Install deps
pip install PyMuPDF mammoth

# Run
python matcher.py resume.txt job.txt
```

**Sample Output**:
```
✅ Resume–Job Match Score: 85.2%
👍 Good fit, minor improvements possible.

📋 Why it may not match (top gaps):
  • Missing 'sql' (job: 2x, resume: 0x)
  • Missing 'database' (job: 1x, resume: 0x)
```

### Web UI
1. Open `index.html` in browser
2. Upload resume + job files
3. Get instant score + recommendations!

## 🛠 Installation

### Python CLI
```bash
pip install PyMuPDF mammoth
```

### Web
- No install! Pure HTML/JS + CDN libs (PDF.js, Mammoth)
- Works offline after first load

## 🎯 Usage Examples

**Files Provided**:
- `resume.txt`: Python/ML Developer resume
- `job.txt`: Sample job req

```bash
python matcher.py resume.txt job.txt
```

**Expected**: ~85% match score 🎯

## 🔬 How It Works

1. **Extract**: Text from TXT/PDF/DOCX
2. **Clean**: Lowercase, remove punctuation/stopwords
3. **Vectorize**: Term Frequency (TF) vectors
4. **Score**: Cosine similarity → 0-100% match
5. **Analyze**: Job keywords missing from resume

**Math**: `cos(θ) = (A·B) / (|A| |B|)`

## 📊 Sample Results

| Score | Status | Example Action |
|-------|--------|----------------|
| 80-100% | 🎉 Excellent | Ready to apply! |
| 60-79% | 👍 Good | Add 1-2 keywords |
| <60% | ⚠️ Revise | Major gaps |

## 🖥 Web Demo
![Web UI](screenshots/web-ui.png)
*(Add screenshot of index.html in action)*

## 🤖 Limitations
- Simple TF-based (no BERT/embeddings)
- English only
- No semantic understanding (exact keywords)

## 🚀 Future Enhancements
- [ ] AI summaries (GPT)
- [ ] Multi-language
- [ ] Resume auto-edits
- [ ] ATS score prediction

## 📝 Sample Files
- `resume.txt` - Python/ML dev resume
- `job.txt` - Python dev job desc

## 📄 License
MIT - Use freely!

**Made by Vansh Parate** ❤️ *using Python + Vanilla JS*

