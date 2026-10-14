import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, KeepTogether
)
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY

def create_script_pdf():
    pdf_path = r"C:\Users\thom\.gemini\antigravity\scratch\edutrack\Naskah_Presentasi_Video_5_Menit_Ikhwan_Nur_Rizki_Fathama.pdf"
    
    # A4 Dimensions: 595.27 x 841.89 points
    # Usable width with 36pt margins = 595.27 - 72 = 523.27 pt
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=A4,
        leftMargin=36,
        rightMargin=36,
        topMargin=36,
        bottomMargin=36
    )

    styles = getSampleStyleSheet()

    # Color Palette (Academic Modern)
    PRIMARY = colors.HexColor("#1E3A8A")   # Deep Indigo
    ACCENT = colors.HexColor("#059669")    # Emerald Green
    TEXT_DARK = colors.HexColor("#0F172A")
    TEXT_MUTED = colors.HexColor("#475569")
    BG_LIGHT = colors.HexColor("#F8FAFC")
    BORDER_COLOR = colors.HexColor("#CBD5E1")

    # Typography Styles
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=16,
        leading=20,
        textColor=PRIMARY,
        alignment=TA_CENTER
    )

    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=15,
        textColor=ACCENT,
        alignment=TA_CENTER
    )

    meta_style = ParagraphStyle(
        'DocMeta',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=TEXT_MUTED,
        alignment=TA_CENTER
    )

    h1_style = ParagraphStyle(
        'Heading1_Custom',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        textColor=PRIMARY,
        spaceBefore=10,
        spaceAfter=4
    )

    body_style = ParagraphStyle(
        'Body_Custom',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9,
        leading=13,
        textColor=TEXT_DARK,
        alignment=TA_JUSTIFY,
        spaceBefore=2,
        spaceAfter=3
    )

    th_style = ParagraphStyle(
        'TableHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9,
        leading=12,
        textColor=colors.white,
        alignment=TA_CENTER
    )

    cell_time_style = ParagraphStyle(
        'CellTime',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11.5,
        textColor=PRIMARY,
        alignment=TA_CENTER
    )

    cell_action_style = ParagraphStyle(
        'CellAction',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11.5,
        textColor=TEXT_DARK
    )

    cell_dialog_style = ParagraphStyle(
        'CellDialog',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=8.5,
        leading=12,
        textColor=colors.HexColor("#1E293B")
    )

    tip_style = ParagraphStyle(
        'TipText',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12,
        textColor=TEXT_DARK
    )

    story = []

    # Title & Metadata Header
    story.append(Paragraph("NASKAH LENGKAP & PANDUAN VIDEO PRESENTASI (5 MENIT)", title_style))
    story.append(Spacer(1, 3))
    story.append(Paragraph("Aplikasi EduTrack: Student Academic & Skill Portfolio Tracker", subtitle_style))
    story.append(Spacer(1, 4))
    
    meta_text = (
        "<b>Penyusun:</b> Ikhwan Nur Rizki Fathama (NIM: 24SA11A023) &nbsp;|&nbsp; "
        "<b>Dosen:</b> Nandang Hermanto, M.Kom.<br/>"
        "<b>Prodi:</b> Informatika, Universitas Amikom Purwokerto &nbsp;|&nbsp; "
        "<b>Mata Kuliah:</b> Pemrograman Mobile Lanjut (Pertemuan 1)"
    )
    story.append(Paragraph(meta_text, meta_style))
    story.append(Spacer(1, 6))
    story.append(HRFlowable(width="100%", thickness=1.5, color=PRIMARY, spaceBefore=2, spaceAfter=8))

    # Konsep Setup Video
    story.append(Paragraph("1. Konsep & Setup Tampilan Rekaman (Live-Coding Style)", h1_style))
    setup_desc = (
        "Video presentasi dirancang berdurasi tepat <b>5 Menit (300 Detik)</b> dengan format teknis modern: "
        "<b>Layar Penuh (Screen Share VS Code & Browser)</b> yang dipadukan dengan <b>Webcam Wajah (Picture-in-Picture)</b> di pojok layar. "
        "Format ini merefleksikan penguasaan materi secara nyata melalui ulasan arsitektur data, demonstrasi interaktif aplikasi, "
        "serta penjelasan solusi atas 4 pertanyaan pemicu modul."
    )
    story.append(Paragraph(setup_desc, body_style))
    story.append(Spacer(1, 6))

    # Rundown & Storyboard Table (Width: 95 + 165 + 263 = 523 pt)
    story.append(Paragraph("2. Matriks Rundown, Aksi Layar, dan Naskah Dialog Lisan", h1_style))

    table_data = [
        [
            Paragraph("Waktu & Segmen", th_style),
            Paragraph("Aksi Layar & Kursor (Visual Action)", th_style),
            Paragraph("Naskah Lisan Lengkap (Dialog)", th_style)
        ],
        # Segmen 1
        [
            Paragraph("<b>00:00 - 00:35</b><br/>(35 Detik)<br/><br/><i>1. Pembukaan & Identitas</i>", cell_time_style),
            Paragraph(
                "• <b>Layar:</b> Tampilkan VS Code terbuka di <code>main.dart</code>.<br/>"
                "• <b>Webcam:</b> Wajah aktif di pojok kanan bawah/atas.<br/>"
                "• <b>Kursor:</b> Menunjuk judul kode secara tenang.",
                cell_action_style
            ),
            Paragraph(
                "\"Halo, selamat pagi/siang Bapak Nandang Hermanto dan rekan-rekan semua. "
                "Perkenalkan, nama saya <b>Ikhwan Nur Rizki Fathama</b> dengan NIM <b>24SA11A023</b> "
                "dari Program Studi Informatika, Universitas Amikom Purwokerto.<br/><br/>"
                "Pada video kali ini, saya akan mempresentasikan hasil pengerjaan latihan praktikum dan pretest "
                "pertemuan pertama mata kuliah Pemrograman Mobile Lanjut, yaitu aplikasi "
                "<b>EduTrack: Student Academic & Skill Portfolio Tracker</b> berbasis Flutter.\"",
                cell_dialog_style
            )
        ],
        # Segmen 2
        [
            Paragraph("<b>00:35 - 01:45</b><br/>(70 Detik)<br/><br/><i>2. Arsitektur Data 1-to-N</i>", cell_time_style),
            Paragraph(
                "• <b>Layar:</b> Buka explorer <code>lib/</code>.<br/>"
                "• Buka <code>models/student_model.dart</code>.<br/>"
                "• <b>Kursor:</b> Sorot <code>List&lt;Certification&gt;</code>.<br/>"
                "• Buka <code>data/dummy_data.dart</code>, sorot list 5 sertifikasi Budi Santoso.",
                cell_action_style
            ),
            Paragraph(
                "\"Untuk memenuhi kriteria kode yang bersih dan modular, struktur proyek saya bagi ke dalam modul: "
                "<code>models</code>, <code>data</code>, <code>screens</code>, dan <code>main.dart</code>.<br/><br/>"
                "<i>(Tunjukkan student_model.dart)</i><br/>"
                "Sesuai instruksi modul mengenai relasi <b>One-to-Many</b>, saya merancang dua model:<br/>"
                "1. <code>Certification</code> sebagai entitas relasi (title, issuer, year, grade).<br/>"
                "2. <code>Student</code> sebagai entitas utama yang menampung NIM, nama, jurusan, email, foto profil, dan properti <code>List&lt;Certification&gt;</code>.<br/><br/>"
                "<i>(Tunjukkan dummy_data.dart)</i><br/>"
                "Pada <code>dummy_data.dart</code>, setiap profil mahasiswa telah menampung sekurang-kurangnya <b>5 data sertifikasi terstruktur</b>, mulai dari Flutter Developer hingga BNSP.\"",
                cell_dialog_style
            )
        ],
        # Segmen 3
        [
            Paragraph("<b>01:45 - 03:10</b><br/>(85 Detik)<br/><br/><i>3. Live Demo Aplikasi</i>", cell_time_style),
            Paragraph(
                "• <b>Layar:</b> Buka browser <code>http://localhost:8080</code>.<br/>"
                "• <b>Aksi 1:</b> Scroll daftar Layar 1.<br/>"
                "• <b>Aksi 2:</b> Klik kartu <i>Budi Santoso</i>.<br/>"
                "• <b>Aksi 3:</b> Layar 2 terbuka, scroll 5 sertifikasi ber-badge Emerald Green.<br/>"
                "• <b>Aksi 4:</b> Tekan tombol Back di AppBar.",
                cell_action_style
            ),
            Paragraph(
                "\"<i>(Tampilkan Layar 1)</i><br/>"
                "Sekarang kita masuk ke demonstrasi aplikasi. Pada <b>Layar 1 (StudentListScreen)</b>, "
                "data disajikan dalam bentuk <code>ListView.builder</code> yang dapat digulir. "
                "Mengadopsi tema <b>Material 3 Academic Modern</b> (Deep Indigo & Soft Slate). Setiap kartu menampilkan foto avatar daring, NIM, jurusan, serta chip ringkas total sertifikasi.<br/><br/>"
                "<i>(Klik kartu -> Layar 2)</i><br/>"
                "Ketika kartu diklik, aplikasi mengeksekusi <code>Navigator.push</code> dengan membawa seluruh objek <code>Student</code> ke <b>Layar 2 (StudentDetailScreen)</b> tanpa query ulang ID.<br/><br/>"
                "<i>(Scroll di Layar 2)</i><br/>"
                "Di Layar 2, bagian atas menampilkan Header Profil lengkap. Di bawahnya, aplikasi merender relasi satu-ke-banyak berupa <b>5 riwayat sertifikasi kompetensi</b> dengan badge predikat kelulusan Emerald Green.<br/><br/>"
                "<i>(Tekan Back)</i><br/>"
                "Saat tombol Back ditekan, aplikasi kembali ke layar utama tanpa kehilangan posisi scroll.\"",
                cell_dialog_style
            )
        ],
        # Segmen 4
        [
            Paragraph("<b>03:10 - 04:25</b><br/>(75 Detik)<br/><br/><i>4. Jawaban 4 Pertanyaan Pemicu</i>", cell_time_style),
            Paragraph(
                "• <b>Layar:</b> Tampilkan VS Code di <code>student_detail_screen.dart</code> atau slide ringkas 4 poin pemicu.<br/>"
                "• <b>Kursor:</b> Mengikuti poin 1 sampai 4.",
                cell_action_style
            ),
            Paragraph(
                "\"Selanjutnya, saya akan menjawab <b>4 pertanyaan pemicu analisis mandiri</b> dari modul praktikum:<br/>"
                "<b>1. Struktur Data Fleksibel:</b> Menggunakan Object-Oriented Modeling. Entitas anak diisolasi di dalam model kelas. Menambah atribut baru tidak akan merusak struktur data mahasiswa utama.<br/>"
                "<b>2. Navigasi Efisien:</b> Menerapkan <i>Object Parameter Passing</i> pada <code>Navigator.push</code>. Objek di memori langsung diteruskan ke layar tujuan, menghemat memori dan bebas lag.<br/>"
                "<b>3. Informasi Ringkas & Informatif:</b> Menerapkan strategi <i>Progressive Disclosure</i>; Layar 1 fokus pada data identitas kunci, sedangkan rincian mendalam 5 sertifikasi dialokasikan di Layar 2.<br/>"
                "<b>4. Pengelolaan Relasi 1-to-N:</b> Menggunakan komposisi <i>Nested List</i> terisolasi di dalam wadah entitas induknya dan dirender via <code>ListView.builder</code> bertingkat.\"",
                cell_dialog_style
            )
        ],
        # Segmen 5
        [
            Paragraph("<b>04:25 - 05:00</b><br/>(35 Detik)<br/><br/><i>5. Uji Statis & Penutup</i>", cell_time_style),
            Paragraph(
                "• <b>Layar:</b> Buka Terminal VS Code.<br/>"
                "• Jalankan <code>flutter analyze</code>.<br/>"
                "• <b>Kursor:</b> Sorot <code>No issues found!</code>.<br/>"
                "• <b>Webcam:</b> Tatap kamera untuk penutup.",
                cell_action_style
            ),
            Paragraph(
                "\"<i>(Tunjukkan Terminal)</i><br/>"
                "Terakhir, untuk menguji kualitas kode secara statis, saya menjalankan perintah <code>flutter analyze</code>. "
                "Hasilnya adalah <b>No issues found</b>, yang membuktikan kode bebas dari galat maupun error sintaks.<br/><br/>"
                "<i>(Tatap kamera)</i><br/>"
                "Seluruh source code dan laporan praktikum juga telah berhasil di-push ke repositori GitHub. "
                "Demikian presentasi dari saya, terima kasih banyak atas perhatian Bapak Nandang Hermanto dan rekan-rekan semua. Selamat pagi/siang.\"",
                cell_dialog_style
            )
        ]
    ]

    t_rundown = Table(table_data, colWidths=[95, 165, 263])
    t_rundown.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), PRIMARY),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('GRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('BACKGROUND', (0,1), (-1,1), colors.HexColor("#FFFFFF")),
        ('BACKGROUND', (0,2), (-1,2), colors.HexColor("#F8FAFC")),
        ('BACKGROUND', (0,3), (-1,3), colors.HexColor("#FFFFFF")),
        ('BACKGROUND', (0,4), (-1,4), colors.HexColor("#F8FAFC")),
        ('BACKGROUND', (0,5), (-1,5), colors.HexColor("#FFFFFF")),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))

    story.append(t_rundown)
    story.append(Spacer(1, 8))

    # Tips Teknis Rekaman
    story.append(Paragraph("3. Checklist & Rekomendasi Teknis Pra-Rekaman", h1_style))
    
    tips_box_data = [
        [
            Paragraph(
                "<b>1. Tab Browser Siap:</b> Buka <code>http://localhost:8080</code> sebelum rekaman dimulai agar tidak menunggu loading.<br/>"
                "<b>2. VS Code Siap:</b> Buka file <code>student_model.dart</code>, <code>dummy_data.dart</code>, dan terminal siap ketik <code>flutter analyze</code>.<br/>"
                "<b>3. Aplikasi Perekam:</b> Gunakan OBS Studio (Screen Display + Window Video Capture), Clipchamp, atau Windows Snipping Tool (Win+Shift+R).<br/>"
                "<b>4. Stopwatch Pendamping:</b> Letakkan ponsel di dekat monitor untuk melihat waktu berjalan agar pas di 4:55 - 5:05.<br/>"
                "<b>5. Tautan Repositori GitHub:</b> Pastikan tautan <code>https://github.com/MasThom99/edutrack</code> dicantumkan pada deskripsi video atau laporan.",
                tip_style
            )
        ]
    ]
    t_tips = Table(tips_box_data, colWidths=[523])
    t_tips.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#EFF6FF")),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#93C5FD")),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(t_tips)

    doc.build(story)
    print("PDF File successfully generated at:", pdf_path)

if __name__ == "__main__":
    create_script_pdf()
