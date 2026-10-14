import 'certification_model.dart';

class Student {
  final String id;
  final String name;
  final String major;
  final String email;
  final String imageUrl;
  final List<Certification> certifications;

  const Student({
    required this.id,
    required this.name,
    required this.major,
    required this.email,
    required this.imageUrl,
    required this.certifications,
  });
}
