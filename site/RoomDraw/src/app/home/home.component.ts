import { Student } from './Student'
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

	myInfo: Student = {
		student_id: 1,
		first_name: "alex",
		last_name: "maese",
		random_number: 10,
		grade_level: 3,
		sex: 'M',
		group_id: 1,
		roommate_id: null
	}
  constructor() { }

  ngOnInit() {
  }

}
