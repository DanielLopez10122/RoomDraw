import { Student } from '../Student';
import { Invitations } from '../Invitations';
import { GroupService } from '../group.service';
import { Component, OnInit } from '@angular/core';
import { Location } from '@angular/common';

@Component({
	selector: 'app-group',
	templateUrl: './group.component.html',
	styleUrls: ['./group.component.css']
})
export class GroupComponent implements OnInit {

	constructor(
		private groupService: GroupService,
		private location: Location
	) { }

	members: Student[];
	invites: Invitations[];
	ngOnInit() {
		this.getGroupMembers();
		this.getGroupInvites();
	}

	getGroupMembers(): void {
		if (this.groupService.members == null) {
			this.groupService.getGroupMembers()
				.subscribe(members => this.members = members);
		} else {
			this.members = this.groupService.members;
		}
	}

	leaveGroup(): void {
		this.groupService.leaveGroup().
			subscribe(() => location.reload())
	}

	getGroupInvites(): void {
		if (this.groupService.invites == null) {
			this.groupService.getInvites()
				.subscribe(invitations => this.invites = invitations);
		} else {
			this.invites = this.groupService.invites;
		}
	}

	inviteToGroup(student_id): void {
		this.groupService.inviteToGroup(student_id)
			.subscribe();
	}

	acceptGroupInvite(group_id): void {
		this.groupService.acceptInvite(group_id)
			.subscribe();
	}

	declineGroupInvite(group_id): void {
		this.groupService.declineInvite(group_id)
			.subscribe();
	}
}
