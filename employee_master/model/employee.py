from odoo import fields, models,api,_
from odoo.exceptions import ValidationError, AccessError


class employee_master(models.Model):
    _name = 'employee.master'

    @api.model
    def create(self, vals):
        if vals.get('name', '/') == '/':
            vals['name'] = self.env['ir.sequence'].get('employee.master') or '/'
        return super(employee_master, self).create(vals)

    @api.multi
    @api.constrains('contact')
    def _check_phone_number(self):
        for rec in self:
            if rec.contact and len(rec.contact) != 10:
                raise ValidationError(_("Employee Contact number Should be 10 digites"))
        return True

    @api.multi
    @api.constrains('family_contact')
    def _check_number(self):
        for rec in self:
            if rec.family_contact and len(rec.family_contact) != 10:
                raise ValidationError(_("Family Contact number should be 10 Digites"))
        return True

    @api.multi
    @api.constrains('acc_no')
    def _check_acc_number(self):
        for rec in self:
            if rec.acc_no and len(rec.acc_no) < 10:
                raise ValidationError(_("Account No should noy be less than 10"))
        return True


    name = fields.Char('Employee ID', defult='New', readonly=False, copy=False)
    employee = fields.Many2one('hr.employee','Employee Name')
    department = fields.Char('Department')
    grade = fields.Char('Grade')
    appraisal_date = fields.Date('Appraisal Date')
    emp_status = fields.Selection([('confirmed', 'Confirmed'),
                                  ('probation', 'Probation'), ],
                                  string="Employee Status")
    current_address = fields.Char('Current Address')
    permanent_address = fields.Char('Permanent Address')
    upload_files = fields.Binary('Upload Your ID')
    l1_manager = fields.Char('L1 Manager')
    l2_manager = fields.Char('L2 Manager')
    hod = fields.Char('HOD')
    director = fields.Char('Director')
    acc_no = fields.Char('Bank Account')
    pan_no = fields.Char('PAN Number')
    aadhar_no = fields.Char('Aadhar Number')
    gender = fields.Selection([('female','Female'),
                            ('male', 'Male'),
                            ('others','Others'),],string="Gender")
    location = fields.Char('Location')
    dob = fields.Char('DOB')
    designation = fields.Char('Designation')
    doj = fields.Char('DOJ')
    driving_license = fields.Char('Driving License')
    exit_date = fields.Date('Exit Date')
    wedding_anniversary = fields.Date('Wedding Anniversary')
    resigned = fields.Selection([('yes','YES'),
                            ('no','NO'),],'Resigned')
    sal_details = fields.Char('Salary Details')
    nationality = fields.Char('Nationality')
    personal_email_id = fields.Char('Personal Email ID')
    company_email_id = fields.Char('Company Email ID')
    father_name = fields.Char("Father's Name")
    contact = fields.Char('Contact No')
    emergency_no = fields.Char('Emergency Contact')
    family_contact = fields.Char("Family's Contact No")
    family_details = fields.Char('Family Details')
    previous_employee_details = fields.Char('Previous Employer Details')
    qualification = fields.Char('Qualification')
    expreience_before_joining = fields.Float('Total No Of Working exprience Before joining')
    Upload_resume = fields.Binary('Upload Your CV')
    pf_no = fields.Char('PF No')
    uan_no = fields.Char('UAN No')
    esic_no = fields.Char('ESIC No')
    blood_group = fields.Char('Blood Group')
    attendance_type = fields.Selection([('rfid', 'RFID'),
                                        ('mobile_apps', 'Mobile Apps'), ],
                                        string="Attendance Type")
    probation_date = fields.Date('Probation Evaluation Date')
    resignation_date = fields.Date('Resignation Date')
    bank_name = fields.Char('Bank Name')
    ifsc_code = fields.Char('Bank IFSC Code')
    marital_status = fields.Boolean('Marital Status')
    mother_name = fields.Char("Mother's")
    wife_name = fields.Char("Wife's Name")
    child1_name = fields.Char("Child 1 Name")
    child2_name = fields.Char("Chil 2 Name")
