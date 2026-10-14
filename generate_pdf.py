import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, KeepTogether
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY

def create_edutrack_pdf():
    pdf_filename = r"C:\Users\thom\.gemini\antigravity\scratch\edutrack\EduTrack_Panduan_Presentasi_Tugas.pdf"
    doc = SimpleDocTemplate(
        pdf_filename,
        pagesize=letter,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40
    )

    styles = getSampleStyleSheet()

    # Custom Color Palette (Academic Modern)
    PRIMARY = colors.HexColor("#1E3A8A")  # Deep Indigo
    ACCENT = colors.HexColor("#059669")   # Emerald Green
    TEXT_DARK = colors.HexColor("#0F172A")
    TEXT_MUTED = colors.HexColor("#475569")
    BG_LIGHT = colors.HexColor("#F8FAFC")
    BORDER_COLOR = colors.HexColor("#E2E8F0")

    # Typography Styles
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=22,
        leading=26,
        textColor=PRIMARY,
        alignment=TA_CENTER
    )

    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        textColor=ACCENT,
        alignment=TA_CENTER
    )

    meta_style = ParagraphStyle(
        'DocMeta',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        leading=14,
        textColor=TEXT_MUTED,
        alignment=TA_CENTER
    )

    h1_style = ParagraphStyle(
        'Heading1_Custom',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=14,
        leading=18,
        textColor=PRIMARY,
        spaceBefore=14,
        spaceAfter=6
    )

    h2_style = ParagraphStyle(
        'Heading2_Custom',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=15,
        textColor=ACCENT,
        spaceBefore=8,
        spaceAfter=4
    )

    body_style = ParagraphStyle(
        'Body_Custom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13.5,
        textColor=TEXT_DARK,
        alignment=TA_JUSTIFY,
        spaceBefore=3,
        spaceAfter=4
    )

    dialog_style = ParagraphStyle(
        'Dialog_Custom',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=9,
        leading=13,
        textColor=colors.HexColor("#1E293B"),
        spaceBefore=2,
        spaceAfter=2
    )

    table_header_style = ParagraphStyle(
        'TableHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9,
        leading=12,
        textColor=colors.white,
        alignment=TA_CENTER
    )

    table_cell_style = ParagraphStyle(
        'TableCell',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11.5,
        textColor=TEXT_DARK
    )

    story = []

    # Title & Metadata Header
    story.append(Paragraph("EDUTRACK: PORTFOLIO & ACADEMIC TRACKER", title_style))
    story.append(Spacer(1, 4))
    story.append(Paragraph("Dokumen Panduan Laporan & Naskah Presentasi Video (5 Menit)", subtitle_style))
    story.append(Spacer(1, 4))
    story.append(Paragraph("<b>Mata Kuliah:</b> Pemrograman Mobile Lanjut (Pertemuan 1) &nbsp;|&nbsp; <b>Dosen:</b> Nandang Hermanto", meta_style))
    story.append(Spacer(1, 8))
    story.append(HRFlowable(width="100%", thickness=2, color=PRIMARY, spaceBefore=4, spaceAfter=12))

    # Section 1: Ringkasan Tugas & Identitas Proyek
    story.append(Paragraph("1. Ringkasan Tugas & Konsep Aplikasi", h1_style))
    story.append(Paragraph(
        "Aplikasi <b>EduTrack (Student Academic & Skill Portfolio Tracker)</b> dibangun berbasis framework Flutter untuk memenuhi kriteria latihan praktikum dan pretest Pemrograman Mobile Lanjut. Aplikasi bertindak sebagai direktori profil mahasiswa sekaligus penyaji rekam jejak sertifikasi kompetensi dalam struktur relasi data bertingkat (One-to-Many).",
        body_style
    ))
    story.append(Spacer(1, 6))

    # Section 2: Modul Arsitektur Data 1-to-N
    story.append(Paragraph("2. Arsitektur Data Modular (One-to-Many)", h1_style))
    data_text = """
    Aplikasi memisah model entitas ke dalam struktur terorganisir di folder <code>lib/models/</code>:<br/>
    • <b>Entitas Utama (Student)</b>: Memuat atribut <code>id</code> (NIM), <code>name</code>, <code>major</code>, <code>email</code>, <code>imageUrl</code>, serta menampung <code>List&lt;Certification&gt; certifications</code>.<br/>
    • <b>Entitas Relasi (Certification)</b>: Memuat rincian sertifikat seperti <code>title</code>, <code>issuer</code>, <code>year</code>, dan <code>grade</code> (Predikat kelulusan).
    """
    story.append(Paragraph(data_text, body_style))
    story.append(Spacer(1, 6))

    # Section 3: Jawaban 4 Pertanyaan Pemicu
    story.append(Paragraph("3. Analisis Mandiri (Jawaban 4 Pertanyaan Pemicu Modul)", h1_style))
    
    q_data = [
        [Paragraph("Pertanyaan Pemicu", table_header_style), Paragraph("Analisis & Jawaban Implementasi", table_header_style)],
        [
            Paragraph("<b>1. Merancang Struktur Data Fleksibel?</b>", table_cell_style),
            Paragraph("Menggunakan pendekatan Object-Oriented Modeling. Class <code>Student</code> mengisolasi list objek <code>Certification</code>. Atribut baru dapat ditambahkan tanpa mengubah struktur dasar.", table_cell_style)
        ],
        [
            Paragraph("<b>2. Navigasi Antar Halaman Efisien?</b>", table_cell_style),
            Paragraph("Menerapkan <i>Object Parameter Passing</i> melalui <code>Navigator.push</code>. Objek <code>Student</code> utuh dikirim langsung ke <code>StudentDetailScreen</code> tanpa querying ulang.", table_cell_style)
        ],
        [
            Paragraph("<b>3. Visualisasi Ringkas & Informatif?</b>", table_cell_style),
            Paragraph("Menggunakan pembagian hirarki visual: Layar 1 menampilkan rangkuman (Avatar, NIM, Badge Counter), sedangkan Layar 2 menampilkan rincian lengkap beserta badge status.", table_cell_style)
        ],
        [
            Paragraph("<b>4. Pengelolaan Relasi Data 1-to-N?</b>", table_cell_style),
            Paragraph("Menanamkan <code>List&lt;Certification&gt;</code> pada model mahasiswa dan dirender menggunakan `ListView.builder` bertingkat di layar detail.", table_cell_style)
        ]
    ]

    t_q = Table(q_data, colWidths=[160, 370])
    t_q.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (1,0), PRIMARY),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('GRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('BACKGROUND', (0,1), (-1,1), colors.HexColor("#F1F5F9")),
        ('BACKGROUND', (0,3), (-1,3), colors.HexColor("#F1F5F9")),
        ('PADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_q)
    story.append(Spacer(1, 10))

    # Section 4: Naskah & Storyboard Video 5 Menit
    story.append(Paragraph("4. Rundown & Naskah Presentasi Video (Durasi Tepat 5 Menit / 300 Detik)", h1_style))

    video_table_data = [
        [
            Paragraph("Waktu & Segmen", table_header_style),
            Paragraph("Panduan Aksi Layar (Screen Action)", table_header_style),
            Paragraph("Naskah Lisan (Dialog)", table_header_style)
        ],
        [
            Paragraph("<b>00:00 - 00:45</b><br/>(45 Detik)<br/><i>1. Pendahuluan</i>", table_cell_style),
            Paragraph("Tampilkan Wajah Webcam / Halaman Utama EduTrack di Chrome.", table_cell_style),
            Paragraph("<i>'Selamat Pagi/Siang Pak Nandang Hermanto dan rekan sekalian. Nama saya [Nama] NIM [NIM]. Hari ini saya mempresentasikan EduTrack: Student Academic & Skill Portfolio Tracker untuk memenuhi pretest Pemrograman Mobile Lanjut...'</i>", dialog_style)
        ],
        [
            Paragraph("<b>00:45 - 01:45</b><br/>(60 Detik)<br/><i>2. Arsitektur Kode</i>", table_cell_style),
            Paragraph("Buka VS Code. Tunjukkan folder <code>lib/</code>, <code>student_model.dart</code>, dan <code>certification_model.dart</code>.", table_cell_style),
            Paragraph("<i>'Aplikasi ini menerapkan Clean Code modular (models, data, screens, main). Untuk relasi One-to-Many, class Student menampung List&lt;Certification&gt; sehingga data terstruktur rapi tanpa database eksternal...'</i>", dialog_style)
        ],
        [
            Paragraph("<b>01:45 - 03:30</b><br/>(105 Detik)<br/><i>3. Live Demo UI</i>", table_cell_style),
            Paragraph("Buka browser `http://localhost:8080`. Scroll Layar 1, klik kartu Budi Santoso -> Layar 2 -> tekan Back.", table_cell_style),
            Paragraph("<i>'Pada Layar 1, ditampilkan daftar mahasiswa dalam ListView Material 3 dengan warna Deep Indigo. Saat kartu diklik, Navigator.push membawa objek Student ke Layar 2 yang menampilkan header profil dan 5 sertifikasi ber-badge Emerald Green...'</i>", dialog_style)
        ],
        [
            Paragraph("<b>03:30 - 04:30</b><br/>(60 Detik)<br/><i>4. Analisis Mandiri</i>", table_cell_style),
            Paragraph("Tampilkan ringkasan 4 Pertanyaan Pemicu modul.", table_cell_style),
            Paragraph("<i>'Menjawab 4 pertanyaan pemicu: 1. Struktur fleksibel via OOP. 2. Navigasi efisien via Object Passing. 3. Visual ringkas via Card Hierarchy. 4. Relasi 1-to-N diisolasi pada nested list detail view...'</i>", dialog_style)
        ],
        [
            Paragraph("<b>04:30 - 05:00</b><br/>(30 Detik)<br/><i>5. Penutup</i>", table_cell_style),
            Paragraph("Kembali ke tampilan utama aplikasi / webcam.", table_cell_style),
            Paragraph("<i>'Demikian presentasi aplikasi EduTrack. Seluruh kebutuhan pretest telah berhasil diimplementasikan dengan bersih. Terima kasih atas perhatiannya.'</i>", dialog_style)
        ]
    ]

    t_v = Table(video_table_data, colWidths=[100, 150, 280])
    t_v.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), PRIMARY),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('GRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('BACKGROUND', (0,1), (-1,1), colors.HexColor("#F8FAFC")),
        ('BACKGROUND', (0,3), (-1,3), colors.HexColor("#F8FAFC")),
        ('BACKGROUND', (0,5), (-1,5), colors.HexColor("#F8FAFC")),
        ('PADDING', (0,0), (-1,-1), 5),
    ]))

    story.append(t_v)

    doc.build(story)
    print("PDF File successfully generated at:", pdf_filename)

if __name__ == "__main__":
    create_edutrack_pdf()
