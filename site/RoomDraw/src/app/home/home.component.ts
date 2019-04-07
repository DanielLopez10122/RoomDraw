import { Student } from '../Student'
import { StudentService } from '../student.service'
import { Component, OnInit } from '@angular/core';

@Component({
	selector: 'app-home',
	templateUrl: './home.component.html',
	styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
	myInfo: Student;
	constructor(private studentService: StudentService) { }

	ngOnInit() {
		this.getMyInfo();
	}

	getMyInfo(): void {
		this.studentService.getInfo()
			.subscribe(myInfo => this.myInfo = myInfo);
	}
}
