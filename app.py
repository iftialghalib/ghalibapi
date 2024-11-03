from flask import Flask, request, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

# Data awal siswa
students = {
    "1": {
        "nama": "Ali",
        "kelas": "10A",
        "prodi": "IPA",
        "nomor_induk": "12345"
    },
    "2": {
        "nama": "Budi",
        "kelas": "11B",
        "prodi": "IPS",
        "nomor_induk": "67890"
    },
}

# Endpoint untuk melihat semua data siswa
class StudentList(Resource):
    def get(self):
        return {
            "error": False,
            "message": "Success",
            "count": len(students),
            "students": students
        }

# Endpoint untuk melihat detail siswa berdasarkan ID
class StudentDetail(Resource):
    def get(self, student_id):
        if student_id in students:
            return {
                "error": False,
                "message": "Success",
                "student": students[student_id]
            }
        return {"error": True, "message": "Data Tidak Ada"}, 404

# Endpoint untuk menambahkan data siswa baru
class AddStudent(Resource):
    def post(self):
        data = request.get_json()
        student_id = str(len(students) + 1)
        new_student = {
            "nama": data.get("nama"),
            "kelas": data.get("kelas"),
            "prodi": data.get("prodi"),
            "nomor_induk": data.get("nomor_induk")
        }
        students[student_id] = new_student
        return {
            "error": False,
            "message": "Siswa berhasil ditambahkan",
            "student": new_student
        }, 201

# Endpoint untuk memperbarui data siswa berdasarkan ID
class UpdateStudent(Resource):
    def put(self, student_id):
        if student_id in students:
            data = request.get_json()
            student = students[student_id]
            student["nama"] = data.get("nama", student["nama"])
            student["kelas"] = data.get("kelas", student["kelas"])
            student["prodi"] = data.get("prodi", student["prodi"])
            student["nomor_induk"] = data.get("nomor_induk", student["nomor_induk"])
            return {
                "error": False,
                "message": "Data Siswa Berhasil di Update",
                "student": student
            }
        return {"error": True, "message": "Siswa Tidak Ditemukan"}, 404

# Endpoint untuk menghapus data siswa berdasarkan ID
class DeleteStudent(Resource):
    def delete(self, student_id):
        if student_id in students:
            deleted_student = students.pop(student_id)
            return {
                "error": False,
                "message": "Siswa berhasil dihapus",
                "student": deleted_student
            }
        return {"error": True, "message": "Siswa Tidak ditemukan"}, 404

# Menambahkan endpoint API
api.add_resource(StudentList, '/students')
api.add_resource(StudentDetail, '/students/<string:student_id>')
api.add_resource(AddStudent, '/students/add')
api.add_resource(UpdateStudent, '/students/update/<string:student_id>')
api.add_resource(DeleteStudent, '/students/delete/<string:student_id>')

if __name__ == '__main__':
    app.run(debug=True)
