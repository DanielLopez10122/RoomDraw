import { Component, OnInit } from '@angular/core';

@Component({
	selector: 'app-housing',
	templateUrl: './housing.component.html',
	styleUrls: ['./housing.component.css']
})
export class HousingComponent implements OnInit {

	halls = [
		{id: 0, name: "Lemke Hall", code: "LEM"},
		{id: 1, name: "Newman Hall", code: "NEW"},
		{id: 2, name: "St. Joseph Hall", code: "STJ"},
		{id: 3, name: "St. Michael Hall", code: "STM"},
		{id: 4, name: "Wolf Hall", code: "WOLF"}
	];
	current_plan = null;
	constructor() { }

	ngOnInit() {
		this.loadFloorPlan(0);
	}

	loadFloorPlan(id) {
		this.current_plan = `/assets/floorplans/${this.halls[id].code}.jpg`;
	}
}
