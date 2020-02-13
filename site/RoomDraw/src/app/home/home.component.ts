import { Student } from '../Student';
import { StudentService } from '../student.service';
import { GroupService } from '../group.service';
import { Component, OnInit } from '@angular/core';

@Component({
	selector: 'app-home',
	templateUrl: './home.component.html',
	styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
	myInfo: Student;
	rank: number;

	constructor(
		private studentService: StudentService,
		private groupService: GroupService
	) { }

	ngOnInit() {
		this.getMyInfo();
	}

	getMyInfo(): void {
		this.studentService.getInfo()
			.subscribe(myInfo => this.myInfo = myInfo);
		this.groupService.getGroupsAhead().
			subscribe(rank => this.rank = rank);
	}

	getRank(): void {
		this.groupService.getGroupsAhead()
			.subscribe(rank => this.rank = rank);
	}
}
