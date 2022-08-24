<template>
<div class="row" style="min-height:100vh;">
    <div class="col-lg-3 bg-white p-5 affix" style="color:#2c3e50;">
        <img src="~@/assets/img/profile-photo.jpg" class="img-fluid rounded-circle" alt="Personal Photo" style="max-height: 200px;">
        <div>
            <div class="py-3 h2 fw-bold">Chukwudumebi Nwobi</div>
            <p class="lead fst-italic mb-4">I am an Engineer with interest in Software Engineering, Automation, and Artificial Intelligence.</p>
            <div class="d-flex justify-content-center mb-4">
                <a href="https://linkedin.com/in/chukwudumebi-nwobi"><BIconLinkedin class="h4 contact-icon" /></a>
                <a href="https://github.com/mebi36"><BIconGithub class="contact-icon h4 ms-3" /></a>
                <a href="mailto:chukwudumebinwobi@gmail.com"><BIconEnvelope class="contact-icon h4 ms-3" /></a>
                <a href="tel:+234-706-482-8313"><BIconTelephoneFill class="contact-icon h4 ms-3" /></a>
                <a href="~@/assets/chukwudumebi_nwobi_resume.pdf" download><BIconFileEarmarkPdfFill class="contact-icon h4 ms-3" /></a>
            </div>
        </div>
    </div>
    <div class="col-lg-9 p-5">
        <div class="row">
            <div class="mb-5">
                <h2><span class="me-2 text-warning"><BIconPersonFill /></span>Personal Information</h2>
                <hr>
                <div class="text-start">
                    <p class="pt-1">
                        <ul style="list-style:none;">
                            <li><strong class="me-1">Country of Residence:</strong>Nigeria</li>
                            <li><strong class="me-1">Email:</strong>chukwudumebinwobi@gmail.com</li>
                        </ul>
                    </p>                
                </div>
            </div>
            <div class="mb-5">
                <h2><span class="me-2 text-warning"><BIconHammer /></span>Skills</h2>
                <hr>
                <div class="d-block d-md-flex pt-1 justify-content-center">
                    <div class="me-3"><BIconCheck class="lead me-1"/>Python</div>
                    <div class="me-3"><BIconCheck class="lead me-1"/>Django</div>
                    <div class="me-3"><BIconCheck class="lead me-1"/>JavaScript</div>
                    <div class="me-3"><BIconCheck class="lead me-1"/>VueJS</div>
                    <div class="me-3"><BIconCheck class="lead me-1"/>CSS</div>
                    <div class="me-3"><BIconCheck class="lead me-1"/>Bootstrap</div>
                    <div class="me-3"><BIconCheck class="lead me-1"/>C/C++</div>
                </div>

            </div>
            <div class="mb-5">
                <h2><span class="me-2 text-warning"><BIconKanban /></span> Major Projects</h2>
                <hr>
                <div class="text-start pt-1">
                    <ul style="list-style:none;">
                        <li>
                            <div>
                                <span class="fw-bold h5">2022: Time and Attendance Management System (TAMS)</span>
                                <p>I contributed to the development of an end-to-end biometric attendance solution for Nigerian Universities. The project is backed by 
                                    The Tertiary Education Trust Fund (TETFUND) of Nigeria. The project involved: 
                                    <ul>
                                        <li>The use of Python's TKinter to design software optimized to run on Raspberry PI single-board computers as well as 
                                            regular PCs (Linux, Windows, and MAC OS).</li>
                                        <li>The design of a server software that will serve as an aggregation point of attendance records logged on the node devices.
                                            The server was implemented as a web application enabling authorized Staff to access student attendance that were logged 
                                            during their lectures, as well as other events such as examinations. This was done primarily in Django and VueJS</li>
                                        <li>Implementation of a REST API for synchronization of data between the node 
                                            devices and the server. This was implemented using Django REST framework.</li>
                                    </ul>
                                    </p>
                                <p>Technology Used: Python; Django; Django REST Framework; JavaScript; VueJS; CSS; Bootstrap</p>
                            </div>
                        </li>
                        <li>
                            <div class="pt-4">
                                <span class="fw-bold h5">2020: ECE Exams Office</span>
                                <p>Was part of the team that designed the result management system for the Department of Electronic Engineering in University of Nigeria.
                                    The project involved:
                                    <ul>
                                        <li>Development of an application (structured as a web application but run locally) for management of student results. 
                                            The software was written using Django.</li>
                                        <li>Implementation of functionalities such as generation of student transcript and collation of results in spreadsheet files using Python
                                            libraries like openpyxl and pandas. </li>
                                    </ul>
                                </p>
                                <p>Technology used: Python; Django; Bootstrap;</p>
                            </div>
                        </li>
                    </ul>
                </div>
            </div>
            <div class="mb-5">
                <h2><span class="me-2 text-warning"><BIconPencilSquare /></span> Education</h2>
                <hr>
                <div class="text-start pt-1">
                    <ul style="list-style: none;">
                        <li class="pb-2"><span class="fw-bold me-1">February 2022:</span>Master of Engineering (M.Eng.) Electronic Engineering. <br>
                        University of Nigeria</li>
                        <li><span class="fw-bold me-1">June 2015:</span>Bachelor of Engineering (B.Eng.) Electronic Engineering.<br>
                        University of Nigeria</li>
                    </ul>
                </div>
            </div>
            <div class="mb-5">
                <h2><span class="me-2 text-warning"><BIconBuilding /></span> Work Experience</h2>
                <hr>
                <div class="text-start pt-1">
                    <ul style="list-style:none;">
                        <li>I currently work as a Graduate Assistant at the University of Nigeria</li>
                        <div>
                            <div>Responsibilities:</div>
                            <ul>
                                <li>Teaching Assistant for undergraduate-level courses including an introductory course in computer programming for sophomores, a course on electronic instrumentation and measurement, and a 300-level course on scientific programming.</li>
                                <li>Contribute to the development and maintenance of the Department's result management system since the inception of the system.</li>
                                <li>Provide technical support for virtual and hybrid events of the Department.</li>
                            </ul>
                        </div>
                    </ul>
                </div>
            </div>
        </div>
    </div>
</div>
</template>

<script>
import { 
    BIconLinkedin, 
    BIconTelephoneFill, 
    BIconCheck, 
    BIconBuilding, 
    BIconKanban, 
    BIconHammer, 
    BIconPencilSquare,
    BIconPersonFill,
    BIconEnvelope,
    BIconFileEarmarkPdfFill,
    BIconGithub
} from 'bootstrap-icons-vue'

export default {
    name: 'Resume',
    components: { 
        BIconLinkedin, 
        BIconTelephoneFill, 
        BIconCheck, 
        BIconBuilding, 
        BIconKanban, 
        BIconHammer, 
        BIconPencilSquare,
        BIconPersonFill,
        BIconEnvelope,
        BIconFileEarmarkPdfFill,
        BIconGithub
    },
    mounted() {
        document.title = this.$route.name + ' | MebiHQ'
    }
}
</script>

<style scoped>
.contact-icon {
    color: #2c3e50;
}
</style>