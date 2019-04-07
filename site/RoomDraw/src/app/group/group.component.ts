import { Student } from '../Student';
import { GroupService } from '../group.service';
import { Component, OnInit } from '@angular/core';

@Component({
	selector: 'app-group',
	templateUrl: './group.component.html',
	styleUrls: ['./group.component.css']
})
export class GroupComponent implements OnInit {

	constructor(private groupService: GroupService) { }

	members: Student[];
	ngOnInit() {
		this.getGroupMembers();
	}

	getGroupMembers(): void {
		this.groupService.getGroupMembers()
			.subscribe(groupMembers =>
				this.members = groupMembers);
	}

}
