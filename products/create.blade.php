@extends('products.layout')
@section('content')
<div class="row">
    <div class="col-lg-12 margin-tb">
        <div class="pull-left">
            <h2>Input Data Penduduk</h2>
        </div>
        <div class="pull-right">
            <a class="btn btn-primary" href="{{ route('products.index') }}"> Back</a>
        </div>
    </div>
</div>
@if ($errors->any())
    <div class="alert alert-danger">
        <strong>Whoops!</strong> There were some problems with your input.<br><br>
        <ul>
            @foreach ($errors->all() as $error)
                <li>{{ $error }}</li>
            @endforeach
        </ul>
    </div>
@endif
<form action="{{ route('products.store') }}" method="POST">
    @csrf
     <div class="row">
        <div class="col-xs-12 col-sm-12 col-md-12">
            <div class="form-group">
                <strong>Name:</strong>
                <input type="text" name="name" class="form-control" placeholder="Name">
            </div>
            <div>
                <strong>NIK:</strong>
                <input type="text" name="nik" class="form-control" placeholder="NIK">
            </div>
            <div>
                <strong>Tempat Tanggal Lahir:</strong>
                <input type="text" name="TTL" class="form-control" placeholder="Tempat Tanggal Lahir">
            </div>
            <div>
                <strong>Jenis Kelamin(L/K):</strong>
                <input type="text" name="kelamin" class="form-control" placeholder="Jenis Kelamin">
            </div>
            <div>
                <strong>Alamat:</strong>
                <input type="text" name="alamat" class="form-control" placeholder="Alamat">
            </div>
            <div>
                <strong>Agama:</strong>
                <input type="text" name="agama" class="form-control" placeholder="Agama">
            </div>
            <div>
                <strong>Status Perkawinan:</strong>
                <input type="text" name="status" class="form-control" placeholder="Status Perkawinan">
            </div>
            <div>
                <strong>Pekerjaan:</strong>
                <input type="text" name="pekerjaan" class="form-control" placeholder="Pekerjaan">
            </div>
            <div>
                <strong>Kewarganegaraan:</strong>
                <input type="text" name="warga" class="form-control" placeholder="Kewarganegaraan">
            </div>
            <div>
                <strong>Masa Berlaku:</strong>
                <input type="text" name="periode" class="form-control" placeholder="Berlaku Hingga">
            </div>
        </div>
        <div class="col-xs-12 col-sm-12 col-md-12">
            <div class="form-group">
                <strong>Detail:</strong>
                <textarea class="form-control" style="height:150px" name="detail" placeholder="Detail"></textarea>
            </div>
        </div>
        <div class="col-xs-12 col-sm-12 col-md-12 text-center">
                <button type="submit" class="btn btn-primary">Submit</button>
        </div>
    </div>
</form>
@endsection