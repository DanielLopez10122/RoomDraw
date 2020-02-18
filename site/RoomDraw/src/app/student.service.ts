import { Student } from './Student'
import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { share } from 'rxjs/operators';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Injectable({
	providedIn: 'root'
})
export class StudentService {

	myInfo: Student;

	httpOptions = {
		headers: new HttpHeaders({
			'SESSION-ID': 'alex'
		})
	}

	constructor(
		private http: HttpClient
	) { }

	getInfo(): Observable<Student> {
		if (this.myInfo != null) {
			return of(this.myInfo)
		}

		var url = "http://localhost:8000/myinfo";
		var obs = this.http.get<Student>(url, this.httpOptions).pipe(share());
		obs.subscribe(myInfo => this.myInfo = myInfo);
		return obs;
	}

	getStudentInfo(student_id): Observable<Student> {
		var url = 'http://localhost:8000/student?id=' + student_id;
		return this.http.get<Student>(url, this.httpOptions);
	}
}
