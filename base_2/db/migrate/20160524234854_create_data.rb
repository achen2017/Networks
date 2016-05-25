class CreateData < ActiveRecord::Migration
  def change
    create_table :data do |t|
      t.integer :query_id
      t.string :module
      t.string :word

      t.timestamps null: false
    end
  end
end
