import java.lang.reflect.Field;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.ArrayList;
import java.util.List;

public class DateReader {

	public IReport readerRkd(String reportid) throws Exception {
		Rkd rkd = new Rkd();
		Connection conn = getConnection();
		String strSql = "SELECT *  FROM rkd where rkd_no=?";
		PreparedStatement stmt = conn.prepareStatement(strSql);
		stmt.setString(1, reportid);
		ResultSet rs = stmt.executeQuery();
		try {
			if (rs.next()) {
				copyRsToObj(rs, rkd);

			}
		} finally {
			rs.close();
			stmt.close();
		}

		List<RkdDetail> rkdList = new ArrayList<RkdDetail>();
		strSql = "SELECT *  FROM rkd_list where rkd_no=?";
		stmt = conn.prepareStatement(strSql);
		stmt.setString(1, reportid);
		rs = stmt.executeQuery();
		try {
			while (rs.next()) {
				RkdDetail rkdDetail = new RkdDetail();
				copyRsToObj(rs, rkdDetail);
				rkdList.add(rkdDetail);
			}
		} finally {
			rs.close();
			stmt.close();
			conn.close();
		}
		rkd.setRkdList(rkdList);
		return rkd;
	}

	public IReport readerFld(String reportid) throws Exception {
		Fld fld = new Fld();
		Connection conn = getConnection();
		String strSql = "SELECT fld_no, khmc, khdz, lxdh, ssds, xqdh, lsh, " 
            + "zdrq, ckrq, flck, jedx, jehj  FROM fld where fld_no=?";
		PreparedStatement stmt = conn.prepareStatement(strSql);
		stmt.setString(1, reportid);
		ResultSet rs = stmt.executeQuery();
		try {
			if (rs.next()) {

				copyRsToObj(rs, fld);

			}
		} catch( Exception e) {
			e.printStackTrace();
		} finally {
			rs.close();
			stmt.close();
		}

		List<FldDetail> fldList = new ArrayList<FldDetail>();
		strSql = "SELECT fld_no, bh, mcjgg, jxdm, jldw, yfsl, sfsl, bz"
				+ " FROM fld_list where fld_no=?";
		stmt = conn.prepareStatement(strSql);
		stmt.setString(1, reportid);
		rs = stmt.executeQuery();
		try {
			while (rs.next()) {
				FldDetail fldDetail = new FldDetail();
				copyRsToObj(rs, fldDetail);
				fldList.add(fldDetail);
			}
		} catch( Exception e) {
			e.printStackTrace();
		} finally {
			rs.close();
			stmt.close();
			conn.close();
		}
		fld.setFldList(fldList);
		return fld;
	}

	/*
	public Connection getConnection() {
		Connection conn = null;
		String url = "jdbc:mysql://localhost:3306/";
		String dbName = "report";
		String driver = "com.mysql.jdbc.Driver";
		String userName = "root";
		String password = "root";
		try {
			Class.forName(driver).newInstance();
			conn = DriverManager.getConnection(url + dbName, userName, password);
		} catch (Exception e) {
			e.printStackTrace();
		}
		return conn;
	}
	*/
	
	public Connection getConnection() {
		Connection conn = null;

		// SQLite
		String driver = "org.sqlite.JDBC";
		String url = "jdbc:sqlite:test.db";
		try {
			Class.forName(driver);
			conn = DriverManager.getConnection(url);
		} catch (Exception e) {
			e.printStackTrace();
		}
		return conn;
	}

	public static void main(String argv[]) throws Exception {
		DateReader da = new DateReader();
		IReport rkd = da.readerRkd("1");
		PdfFiels.manipulatePdf("G:\\rkd.pdf", "G:\\fld001.pdf", rkd);
	}

	public void copyRsToObj(ResultSet rs, Object obj) throws Exception {
		for (Field fd : obj.getClass().getDeclaredFields()) {
			if (fd.getName().endsWith("List"))
				continue;
			fd.set(obj, rs.getString(fd.getName()));
		}
	}

	public IReport readerSld(String reportid) throws Exception {
		Sld sld = new Sld();
		Connection conn = getConnection();
		String strSql = "SELECT *  FROM sld where sld_no=?";
		PreparedStatement stmt = conn.prepareStatement(strSql);
		stmt.setString(1, reportid);
		ResultSet rs = stmt.executeQuery();
		try {
			if (rs.next()) {
				copyRsToObj(rs, sld);

			}
		} finally {
			rs.close();
			stmt.close();
		}

		List<SldDetail> sldList = new ArrayList<SldDetail>();
		strSql = "SELECT *  FROM sld_list where sld_no=?";
		stmt = conn.prepareStatement(strSql);
		stmt.setString(1, reportid);
		rs = stmt.executeQuery();
		try {
			while (rs.next()) {
				SldDetail sldDetail = new SldDetail();
				copyRsToObj(rs, sldDetail);
				sldList.add(sldDetail);
			}
		} finally {
			rs.close();
			stmt.close();
			conn.close();
		}
		sld.setSldList(sldList);
		return sld;
	}

	public IReport readerJld(String reportid) throws Exception {
		Jld jld = new Jld();
		Connection conn = getConnection();
		String strSql = "SELECT *  FROM jld where jld_no=?";
		PreparedStatement stmt = conn.prepareStatement(strSql);
		stmt.setString(1, reportid);
		ResultSet rs = stmt.executeQuery();
		try {
			if (rs.next()) {
				copyRsToObj(rs, jld);

			}
		} finally {
			rs.close();
			stmt.close();
		}

		List<JldDetail> jldList = new ArrayList<JldDetail>();
		strSql = "SELECT *  FROM jld_list where jld_no=?";
		stmt = conn.prepareStatement(strSql);
		stmt.setString(1, reportid);
		rs = stmt.executeQuery();
		try {
			while (rs.next()) {
				JldDetail jldDetail = new JldDetail();
				copyRsToObj(rs, jldDetail);
				jldList.add(jldDetail);
			}
		} finally {
			rs.close();
			stmt.close();
			conn.close();
		}
		jld.setJldList(jldList);
		return jld;
	}

	public IReport readerLyd(String reportid) throws Exception {
		Lyd lyd = new Lyd();
		Connection conn = getConnection();
		String strSql = "SELECT *  FROM lyd where lyd_no=?";
		PreparedStatement stmt = conn.prepareStatement(strSql);
		stmt.setString(1, reportid);
		ResultSet rs = stmt.executeQuery();
		try {
			if (rs.next()) {
				copyRsToObj(rs, lyd);

			}
		} finally {
			rs.close();
			stmt.close();
		}

		List<LydDetail> lydList = new ArrayList<LydDetail>();
		strSql = "SELECT *  FROM lyd_list where lyd_no=?";
		stmt = conn.prepareStatement(strSql);
		stmt.setString(1, reportid);
		rs = stmt.executeQuery();
		try {
			while (rs.next()) {
				LydDetail lydDetail = new LydDetail();
				copyRsToObj(rs, lydDetail);
				lydList.add(lydDetail);
			}
		} finally {
			rs.close();
			stmt.close();
			conn.close();
		}
		lyd.setLydList(lydList);
		return lyd;
	}

	public IReport readerNbdbd(String reportid) throws Exception {
		Nbdbd nbdbd = new Nbdbd();
		Connection conn = getConnection();
		String strSql = "SELECT *  FROM nbdbd where nbdbd_no=?";
		PreparedStatement stmt = conn.prepareStatement(strSql);
		stmt.setString(1, reportid);
		ResultSet rs = stmt.executeQuery();
		try {
			if (rs.next()) {
				copyRsToObj(rs, nbdbd);

			}
		} finally {
			rs.close();
			stmt.close();
		}

		List<NbdbdDetail> nbdbdList = new ArrayList<NbdbdDetail>();
		strSql = "SELECT *  FROM nbdbd_list where nbdbd_no=?";
		stmt = conn.prepareStatement(strSql);
		stmt.setString(1, reportid);
		rs = stmt.executeQuery();
		try {
			while (rs.next()) {
				NbdbdDetail nbdbdDetail = new NbdbdDetail();
				copyRsToObj(rs, nbdbdDetail);
				nbdbdList.add(nbdbdDetail);
			}
		} finally {
			rs.close();
			stmt.close();
			conn.close();
		}
		nbdbd.setNbdbdList(nbdbdList);
		return nbdbd;
	}

}
