import { Student } from './Student';
import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Injectable({
	providedIn: 'root'
})
export class GroupService {

	httpOptions = {
		headers: new HttpHeaders({
			'SESSION-ID': 'alex'
		})
	}
	url = "http://localhost:8000/group/members";
	constructor(
		private http: HttpClient
	) { }

	getGroupMembers(): Observable<Student[]> {
		return this.http.get<Student[]>(this.url, this.httpOptions);
	}
}
