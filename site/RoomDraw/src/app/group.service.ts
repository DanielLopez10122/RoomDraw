import { Student } from './Student';
import { Invitations } from './Invitations';
import { StudentService } from './student.service';
import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { HttpClient, HttpHeaders, HttpParams } from '@angular/common/http';

@Injectable({
	providedIn: 'root'
})
export class GroupService {

	public members: Student[];
	public invites: Invitations[];
	httpOptions = {
		headers: new HttpHeaders({
			'SESSION-ID': 'alex'
		})
	}
	constructor(
		private http: HttpClient,
		private studentService: StudentService
	) { }

	getGroupsAhead(): Observable<number> {
		var url = "http://localhost:8000/group/rank";
		return this.http.get<number>(url, this.httpOptions);
	}

	getGroupMembers(): Observable<Student[]> {
		var url = "http://localhost:8000/group/members";

		var obs = this.http.get<Student[]>(url, this.httpOptions);
		obs.subscribe(members => this.members = members);
		return obs;
	}

	leaveGroup(): Observable<Object> {
		var url = "http://localhost:8000/group"
		return this.http.delete<Object>(url, this.httpOptions);
	}

	getInvites(): Observable<Invitations[]> {
		var url = "http://localhost:8000/group/invite";
		return this.http.get<Invitations[]>(url, this.httpOptions);
	}

	inviteToGroup(student_id): Observable<Object> {
		var url = "http://localhost:8000/group/invite";
		const body = {
			student_id: student_id
		}

		var str = JSON.stringify(body)
		return this.http.post<Object>(url, str, this.httpOptions);
	}

	acceptInvite(group_id): Observable<Object> {
		var url = "http://localhost:8000/group/invite";
		const body = {
			group_id: group_id
		}

		var str = JSON.stringify(body)
		return this.http.put<Object>(url, str, this.httpOptions);
	}

	declineInvite(group_id): Observable<Object> {
		var url = "http://localhost:8000/group/invite?group_id=" + group_id;

		return this.http.delete<Object>(url, this.httpOptions);
	}
}
