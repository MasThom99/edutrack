import '../models/student_model.dart';
import '../models/certification_model.dart';

final List<Student> dummyStudents = [
  const Student(
    id: "220101001",
    name: "Budi Santoso",
    major: "Teknik Informatika",
    email: "budi.santoso@student.ac.id",
    imageUrl: "https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=400&q=80",
    certifications: [
      Certification(
        title: "Flutter Mobile Developer Professional",
        issuer: "Dicoding Indonesia",
        year: "2024",
        grade: "Sangat Baik",
      ),
      Certification(
        title: "AWS Certified Cloud Practitioner",
        issuer: "Amazon Web Services",
        year: "2023",
        grade: "Kompeten",
      ),
      Certification(
        title: "Google Associate Android Developer",
        issuer: "Google Developers",
        year: "2023",
        grade: "Grade A",
      ),
      Certification(
        title: "UI/UX Design Specialization",
        issuer: "Coursera / CalArts",
        year: "2022",
        grade: "Distinction",
      ),
      Certification(
        title: "Junior Web Developer (BNSP)",
        issuer: "BNSP Republik Indonesia",
        year: "2022",
        grade: "Kompeten",
      ),
    ],
  ),
  const Student(
    id: "220101002",
    name: "Siti Rahmawati",
    major: "Sistem Informasi",
    email: "siti.rahmawati@student.ac.id",
    imageUrl: "https://images.unsplash.com/photo-1494790108377-be9c29b29330?auto=format&fit=crop&w=400&q=80",
    certifications: [
      Certification(
        title: "Data Analyst Professional Certificate",
        issuer: "Google / Coursera",
        year: "2024",
        grade: "Grade A",
      ),
      Certification(
        title: "Certified Information Systems Auditor (CISA)",
        issuer: "ISACA",
        year: "2024",
        grade: "Sangat Baik",
      ),
      Certification(
        title: "SQL & Relational Database Masterclass",
        issuer: "Oracle Academy",
        year: "2023",
        grade: "Kompeten",
      ),
      Certification(
        title: "IT Project Management Fundamentals",
        issuer: "Project Management Institute (PMI)",
        year: "2023",
        grade: "Grade A",
      ),
      Certification(
        title: "Business Process Modeling (BPMN)",
        issuer: "BPM Institute",
        year: "2022",
        grade: "Kompeten",
      ),
    ],
  ),
  const Student(
    id: "220101003",
    name: "Rian Hidayat",
    major: "Teknik Komputer",
    email: "rian.hidayat@student.ac.id",
    imageUrl: "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=400&q=80",
    certifications: [
      Certification(
        title: "Cisco Certified Network Associate (CCNA)",
        issuer: "Cisco Systems",
        year: "2024",
        grade: "Grade A+",
      ),
      Certification(
        title: "CompTIA Security+ Certification",
        issuer: "CompTIA",
        year: "2024",
        grade: "Kompeten",
      ),
      Certification(
        title: "Internet of Things (IoT) Systems Specialist",
        issuer: "Intel Academy",
        year: "2023",
        grade: "Sangat Baik",
      ),
      Certification(
        title: "Linux System Administrator",
        issuer: "Red Hat Academy",
        year: "2023",
        grade: "Kompeten",
      ),
      Certification(
        title: "Ethical Hacking Fundamentals",
        issuer: "EC-Council",
        year: "2022",
        grade: "Grade A",
      ),
    ],
  ),
  const Student(
    id: "220101004",
    name: "Amanda Putri",
    major: "Sains Data",
    email: "amanda.putri@student.ac.id",
    imageUrl: "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?auto=format&fit=crop&w=400&q=80",
    certifications: [
      Certification(
        title: "Machine Learning Engineering",
        issuer: "DeepLearning.AI",
        year: "2024",
        grade: "Honors",
      ),
      Certification(
        title: "TensorFlow Developer Certificate",
        issuer: "Google Cloud",
        year: "2024",
        grade: "Grade A",
      ),
      Certification(
        title: "Python for Data Science & AI",
        issuer: "IBM Skills Network",
        year: "2023",
        grade: "Sangat Baik",
      ),
      Certification(
        title: "Big Data Foundation Certification",
        issuer: "Cloudera",
        year: "2023",
        grade: "Kompeten",
      ),
      Certification(
        title: "Data Visualization with Tableau",
        issuer: "Tableau Software",
        year: "2022",
        grade: "Kompeten",
      ),
    ],
  ),
];
