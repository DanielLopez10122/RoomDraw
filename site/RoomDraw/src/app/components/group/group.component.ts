import { Student } from '../../models/Student';
import { Invitations } from '../../models/Invitations';
import { StudentService } from '../../services/student.service';
import { GroupService } from '../../services/group.service';
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
		private studentService: StudentService,
		private location: Location
	) { }

	members: Student[];
	invites: Invitations[];

	static idx = 0;

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

	private _populateInviteLeaders(invitations: Invitations[]): void {
		if (invitations == null) {
			return;
		}

		GroupComponent.idx = 0;
		for (var i = 0; i < invitations.length; i++) {
			var id = invitations[i].group_id;
			this.studentService.getStudentInfo(id).
				subscribe(info => invitations[GroupComponent.idx++].leader = info.first_name + ' ' + info.last_name)
		}
	}

	private _populateInvitations(invitations: Invitations[]) {
		this._populateInviteLeaders(invitations);
		this.invites = invitations;
	}

	getGroupInvites(): void {
		if (this.groupService.invites == null) {
			this.groupService.getInvites()
				.subscribe(invitations => this._populateInvitations(invitations));
		} else {
			console.log("Populating null");
			this._populateInvitations(this.groupService.invites);
		}
	}

	inviteToGroup(student_id): void {
		this.groupService.inviteToGroup(student_id)
			.subscribe();
	}

	acceptGroupInvite(group_id): void {
		this.groupService.acceptInvite(group_id)
			.subscribe(() => location.reload());
	}

	declineGroupInvite(group_id): void {
		this.groupService.declineInvite(group_id)
			.subscribe(() => location.reload());
	}
}
