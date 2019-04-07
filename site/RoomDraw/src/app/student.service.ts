import { Student } from './Student'
import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Injectable({
	providedIn: 'root'
})
export class StudentService {

	httpOptions = {
		headers: new HttpHeaders({
			'SESSION-ID': 'alex'
		})
	}
	url = "http://localhost:8000/myinfo";

	constructor(
		private http: HttpClient
	) { }

	getInfo(): Observable<Student> {
		return this.http.get<Student>(this.url, this.httpOptions);
	}
}
